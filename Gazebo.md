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

## Setup X11 Forwarding
This assumes you're on Linux.
Make sure your devcontainer.json looks like this:
```json
...
"runArgs": [
        "--net=host",
        "-it",
        "--device=/dev/ttyACM0", // Or whatever port
        "--privileged",
        // For X
        "--volume=/tmp/.X11-unix:/tmp/.X11-unix",
        "--volume=/home/<your username>/.Xauthority:/home/vscode/.Xauthority",
        "-e DISPLAY=$DISPLAY"
    ],
...
```
Now, on your host machine, run:
```bash
xhost + local:
```
And in the container, run:
```
sudo usermod -a -G video vscode
```
To test if it works, run
```
xeyes
```
If you see a pair of eyes, you're good to go!

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
If it shows some weird error about "QThread", run this instead:
```bash
QT_QPA_PLATFORM=minimal ros2 run virtual_maize_field generate_world
```
In this case, it's not actually using QT to show a window, but to do some weird opencv thing, so using the minimal platform works.

Now launch gazebo:
```bash
ros2 launch virtual_maize_field simulation.launch.py
```
If it seems to launch but doesn't pop up, then the DISPLAY variable is probably wrong.
Go to your host system and find out the display (`echo $DISPLAY`). Now, run Gazebo with the display:
```bash
DISPLAY=:0 ros2 launch virtual_maize_field simulation.launch.py
```

## Launch Gazebo
Now, in the VNC window (if using), and in the `virtual_maize_field` folder, run:
```bash
source install/setup.bash
ros2 launch virtual_maize_field simulation.launch.py
```
Now wait for a few minutes because it runs very very slowly.
