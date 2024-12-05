import launch
import launch_ros.actions

import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.SetEnvironmentVariable('RCUTILS_CONSOLE_OUTPUT_FORMAT', '{message}'),
        launch_ros.actions.Node(
            package='ros_nav',
            executable='motor',
            name='motor',
            output='screen',
        ),
        IncludeLaunchDescription(
            XMLLaunchDescriptionSource([os.path.join(
                get_package_share_directory('rosbridge_server'), 'launch'),
                '/rosbridge_websocket_launch.xml'])
        ),
    ])