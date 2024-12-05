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

## Quickstart

For the quickstart we will use a ROS launchfile to launch the entire navigation stack.

Firstly you will need a ROS2 environment. To get one open the command palette in VS Code and select *Dev Containers: Rebuild and Reopen in Container*.  

Our project is always built and run inside the `nav_workspace` directory. So cd into it:  
`cd nav_workspace`

The three command to build and run our stack are in a shell script, so finally run:
```
./launch.sh
```

Congrats 🥳. The entire navigation stack is running locally on your computer! Head to 
[http://localhost:4173/arm-controls](http://localhost:4173/arm-controls) to remotely control agrobot!

When you interact with the web interface you should see your actions reflected in the terminal like this:
```
[motor-1]  MOTOR NODE  mod:0, dir: -180, spd: -127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: -180, spd: 127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: 180, spd: 127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: 0, spd: 127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: 0, spd: -127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: -180, spd: -127
[motor-1]  NO ARDUINO  not connected through serial
[motor-1]  MOTOR NODE  mod:0, dir: 0, spd: 0
```

The MOTOR NODE line displays the value the ROS MOTOR NODE received. The NO ARDUINO line 
displays the line the arduino send back to us through serial. When no arduino is connected 
we try to run everything as realistically as possible so we replace the arduino response with "not connected through serial".