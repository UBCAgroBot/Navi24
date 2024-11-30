# How to start Gazebo

## Setup VNC
If you want to run it from the container, you will need to setup VNC.

Note that this runs incredibly slowly.

Install VNC:
```bash
sudo apt-get update && sudo apt-get install -qqy x11-apps x11vnc xvfb openbox
mkdir ~/.vnc
x11vnc -storepasswd 1234 ~/.vnc/passwd
```
Start VNC:
```bash
x11vnc -rfbport 5566 -usepw -cr
```
Connect to VNC using your favourite VNC viewer: Point it to `localhost::5566`
This should open an ugly terminal. To start a basic desktop environment, run:
```bash
openbox
```

## Setup Gazebo
Install a bunch of packages:
```bash
pip install matplotlib
pip install --upgrade numpy==1.26.4
pip install shapely
sudo apt-get install ros-humble-ros-gz
sudo apt install ros-humble-ros-ign-gazebo
sudo apt install ros-humble-ros-ign-bridge
```

Navigate to the `virtual_maize_field` folder. Run
```bash
colcon build
source install/setup.bash
ros2 run virtual_maize_field generate_world
```

## Launch Gazebo
Now, in the VNC window (if using), and in the `virtual_maize_field` folder, run:
```
source install/setup.bash
ros2 launch virtual_maize_field simulation.launch.py
```
Now wait for a few minutes because it runs very very slowly.
