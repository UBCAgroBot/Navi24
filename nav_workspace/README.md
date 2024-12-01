# Navigation's ROS Packages

### ros_nav / other nodes:
All of the nodes we write will be in ros_nav. We also have one dependency (rosbridge_server) to run.

**motor_controller**  
Listens for _motor_instruction_ and sends them to the arduino  
`ros2 run ros_nav motor_controller`  

**arduino_listener**
Listens for serial output and prints it to the screen. Its good to have a separate node to listen for serial output so we don't block and important nodes.
`ros2 run ros_nav arduino_listener`  

**rosbridge_server**
Sets up a websocket server on port 9090 to forward ROS messages from the client. This is a dependency that needs to be installed.
`ros2 launch rosbridge_server rosbridge_websocket_launch.xml`

### interfaces:  
Custom interfaces for ROS messages. No code, only definitions in here.  
