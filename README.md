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
Navi24 consists of three subsystems, the frontend, Jetson and Arduino. Frontend runs on the user's personal computer and communicates with ROS using a websocket (right now on ws://localhost:9090). The Arduino is connected to the Jetson. On the Jetson the ROS `motor_controller` node receives `interfaces/msg/Motor` messages and sends them to the Arduino.

Once the Zed cameras arrive they will publish data to ROS and the path planning node will use that info to send messages to the `motor_controller` node.
