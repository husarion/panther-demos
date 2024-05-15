#!/usr/bin/python3
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import LifecycleNode, Node

import os


def generate_launch_description():
    lsc16_driver_params = os.path.join(
        get_package_share_directory("lslidar_driver"), "params", "lslidar_c16.yaml"
    )

    driver_node = LifecycleNode(
        package="lslidar_driver",
        namespace="c16",
        executable="lslidar_c16driver_node",
        name="lslidar_driver_node",
        output="screen",
        emulate_tty=True,
        parameters=[lsc16_driver_params],
    )

    static_tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        arguments=["0.135", "0", "0", "-1.57", "0", "0", "cover_link", "laser_link"],
        output="screen",
    )

    actions = [driver_node, static_tf_node]

    return LaunchDescription(actions)
