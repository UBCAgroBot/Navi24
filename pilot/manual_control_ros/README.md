# Example ros publisher/subscriber package

An example to show off subscriber and publisher model.

### Running the nodes:
~~~
python3 ros_example/ros_example/ImagePublisher.py
python3 ros_example/ros_example/ImgProcessor.py
python3 ros_example/ros_example/MotorController.py
~~~

### Testing:
~~~
colcon build --packages-select ros_example
source install/setup.bash
colcon test --packages-select ros_example
colcon test-result --verbose
~~~

### ROSBRIDGE:
This is a program that lets the frontend javascript communicate to ROS

To run:
```
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```