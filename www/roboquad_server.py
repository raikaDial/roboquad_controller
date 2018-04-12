#!/usr/bin/env python

from flask import Flask, render_template, request
import serial

shift_level = "1"

arduino_port = serial.Serial('/dev/ttyUSB1', 57600)

app = Flask(__name__)

@app.route('/')
def index():
	templateData = {
		'shift_level': shift_level
	}
	return render_template('index.html', **templateData)

@app.route('/<quad_command>')
def commandQuad(quad_command):
	global shift_level
	# If the command is shift, simply store new level
	if quad_command == "shift1":
		shift_level = "1"
	elif quad_command == "shift2":
		shift_level = "2"
	elif quad_command == "shift3":
		shift_level = "3"
	elif quad_command == "shift4":
		shift_level = "4"
	# An actual command, send over serial
	else:
		command = quad_command + shift_level
		arduino_port.write(command.encode())

	templateData = {
    	'shift_level': shift_level
	}

	return render_template('index.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')