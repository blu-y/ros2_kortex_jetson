import os
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():

    launch_arguments = {
        "robot_ip": "192.168.1.10",
        "use_fake_hardware": "false",
        "gripper": "gen3_lite_2f",
        "gripper_joint_name": "right_finger_bottom_joint",
        "dof": "6",
        "gripper_max_velocity": "100.0",
        "gripper_max_force": "100.0",
    }

    moveit_config = (
        MoveItConfigsBuilder("gen3", package_name="kinova_gen3_lite_moveit_config")
        .robot_description(mappings=launch_arguments)
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .planning_scene_monitor(
            publish_robot_description=True, publish_robot_description_semantic=True
        )
        .planning_pipelines(pipelines=["ompl", "pilz_industrial_motion_planner"])
        .to_moveit_configs()
    )
    
    pick_place_demo = Node(
        package="moveit_task_constructor_demo",
        executable="pick_place_demo",
        output="screen",
        parameters=[
            os.path.join(get_package_share_directory("kinova_gen3_lite_moveit_config"), "config", "gen3_lite_pickplace_config.yaml"),
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
        ],
    )

    return LaunchDescription([pick_place_demo])

