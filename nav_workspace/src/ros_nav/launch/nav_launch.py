import launch
import launch_ros.actions

import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='ros_nav',
            executable='motor_controller',
            name='motor_controller',
            output='screen',
        ),
        launch_ros.actions.Node(
            package='ros_nav',
            executable='arduino_listener',
            name='arduino_listener',
            output='screen',
        ),
        IncludeLaunchDescription(
            XMLLaunchDescriptionSource([os.path.join(
                get_package_share_directory('rosbridge_server'), 'launch'),
                '/rosbridge_websocket_launch.xml'])
        ),
    ])