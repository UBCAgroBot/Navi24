#!/usr/bin/bash

# A simple script to start the rosbridge server and the motor_controller node

colcon build
source install/setup.bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml &
ros2 run ros_nav motor_controller
