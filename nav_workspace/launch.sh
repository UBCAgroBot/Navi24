#!/usr/bin/bash

# A simple script to start the rosbridge server and the motor_controller node

colcon build
source install/setup.bash
ros2 launch ros_nav nav_launch.py
