# Navi24
Developed By UBC AgroBot Navigation and Embedded Systems Team

## Background Information
Navi24 is a robot navigation system consisting of software and hardware.
The system will be installed onto Agrobot 2.0, and will result in manual
and autonomous control of the Agrobot. The autonomous control system will
execute the movement of Agrobot in crop fields according to rules described
in the [FRE competition guidelines](https://drive.google.com/file/d/10Hz0DrzzQszidzNPrzO9qI2uGP24eW8k/view?usp=drive_link).
The manual control system will allow a pilot to control the movement of Agrobot remotely.

## Overview
Navi24 consists of three subsystems that run on different devices.
Pilot subsystem runs on the user's personal computer and communicates
with the robot through the internet protocol. Jetson and Arduino
subsystems are installed onto the robot. Jetson pulls data from
sensors and does the heavy processing. Arduino runs the motor
controllers to perform the actions requested by Jetson. Arduino
receives data from the feedback sensors installed with the motors
to ensure the actions are executed correctly.

