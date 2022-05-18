from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.actions import LifecycleNode

from launch import LaunchContext
from launch.actions import SetEnvironmentVariable
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration

import os



package_dir = get_package_share_directory('ros2_laser_scan_matcher')

# get path to params file
matcher_params_path = os.path.join(
    package_dir,
    'params',
    'matcher.yaml'
)

def generate_launch_description():

    simulation = os.environ.get('SIMULATION')
    if simulation in [None, '']:
        simulation = 'False'

    return LaunchDescription([
        Node(
            package='ros2_laser_scan_matcher',
            executable='laser_scan_matcher',
            output="screen",
            name='laser_scan_matcher',
            namespace="laser_scan_matcher",
            parameters=[matcher_params_path],
        ),
    ])

    
