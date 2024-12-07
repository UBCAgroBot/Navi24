#!/usr/bin/bash

sudo apt-get update && \
    sudo apt-get install -y ros-humble-rosbridge-suite python3-opencv python3-serial python3-rosdep ros-humble-cv-bridge nodejs npm && \
    sudo rm -rf /var/lib/apt/lists/*

sudo npm install -g n

sudo n stable

hash -r

sudo rosdep init && sudo rosdep update

pip install omegaconf