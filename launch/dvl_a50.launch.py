from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('ip_address', default_value='192.168.194.95'),
        DeclareLaunchArgument('namespace', default_value='dvl_a50'),
        DeclareLaunchArgument('frame_id', default_value='dvl_a50_link'),

        
        Node(
            package='dvl_a50', 
            executable='dvl_a50_sensor', 
            namespace=LaunchConfiguration('namespace'),
            output='screen',
            parameters=[{'dvl_ip_address': LaunchDescription('ip_address'),
                         'velocity_frame_id': LaunchConfiguration('frame_id'),
                         'position_frame_id': LaunchConfiguration('frame_id')}],
        )
    ])
       
