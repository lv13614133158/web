from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    params_file = get_package_share_directory('my_libas_cam') + '/config/camera_0.yaml'
    print(params_file)
    return LaunchDescription([
        Node(
            package='my_libas_cam',
            executable='my_libas_cam',
            name='my_libas_cam',
            output='screen',
            parameters=[params_file]
        )
    ])
