# Navigation's ROS Packages
Build with:
~~~
colcon build
source install/setup.bash
~~~

### interfaces:  
Custom interfaces for ROS messages. No code, only definitions in here.  

### ros_nav:  
ROS nodes, this is where our code lives.  
Its nodes are:  

**motor_controller**  
Listens for _motor_instruction_ and sends them to the aurduino  
`ros2 run ros_nav motor_controller`  

**drive_forward**  
Continually sends *motor_instruction*'s to drive forward  
`ros2 run ros_nav drive_forward`

### rosbridge_server:  
External ros package to listen for frontend requests.  
Install with: `sudo apt install ros-humble-rosbridge_server`  
Run with: `ros2 launch rosbridge_server rosbridge_websocket_launch.xml`  