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

For the quickstart we will run the frontend, the ros server and the motor controller to see how a request goes from the frontend to the aurduino.

Firstly you will need a ROS2 environment. To get one open the command palette in VS Code and select *Dev Containers: Rebuild and Reopen in Container*.  
In the container's terminal run:  

~~~
colcon build
source install/setup.bash
ros2 launch ros_nav nav_launch.py
~~~

Finally in a new terminal outside of the ros evironment start the frontend:  
~~~
cd frontend
pnpm i
pnpm dev
~~~

When you use the web interface you will see the `motor_controller` node printing the motor instructions it receives 🥳.