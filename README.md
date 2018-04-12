# Roboquad Controller

This repository contains a hardware/firmware/software package to allow for control of a 2007 Roboquad from WowWee Robotics. 

## Directories
- **firmware**: Contains sketch for Arduino Uno or Mega which parses commands from the usb port and transmits them to the robot. Commands are transmitted over USB at 57600 baud and each command consists of three ASCII characters, the first two specifying the command and the last specifying the shift level of that command. The specific ASCII codes can be discovered by reading the source code, should the user want to control the robot from a serial terminal.

- **www**: Emulates the original robot remote control with a web interface. Using Python, install flask and pyserial, then run *roboquad_server.py*. Interface will be accessible with your web browser at *127.0.0.1:5000*. You may have to edit *roboquad_server.py* to set the Arduino port name to the appropriate value (e.g. */dev/ttyACM0*). The IR detector for the robot is located in its head, so when you send the command the robot will have to be looking right at the controller.

- **hardware**: Contains sketch of controller circuit schematic and a picture of a prototype. Uses a 555 timer to generate the 39.2 kHz carrier wave for the IR communication. Timer is toggled on and off by pin 8 of the Arduino, modulating the IR light to transmit data. Being super precise with the resistors seems to be unnecessary, as the robot seems to work as long as the frequency is within +- 1 kHz.