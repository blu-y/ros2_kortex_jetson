# Jetpack 6.0 & Gen3 Lite
The gen3_lite.launch.py launch file is designed to be used for Gen3 Lite arms. The typical use case to bringup the robot arm:

```bash
ros2 launch kortex_bringup gen3_lite.launch.py
```

For the Gen3 Lite arm, the integrated gripper is considered as a joint, so to command it, it must be included in the joint_names array. (0.0=open, 1.0=close):

```bash
ros2 topic pub /joint_trajectory_controller/joint_trajectory trajectory_msgs/JointTrajectory "{
  joint_names: [joint_1, joint_2, joint_3, joint_4, joint_5, joint_6, right_finger_bottom_joint],
  points: [
    { positions: [0, 0, 0, 0, 0, 0, 1], time_from_start: { sec: 10 } },
  ]
}" -1
```

You can also command the arm using Twist messages. Before doing so, you must active the `twist_controller` and deactivate the `joint_trajectory_controller`:

```bash
ros2 service call /controller_manager/switch_controller controller_manager_msgs/srv/SwitchController "{
  activate_controllers: [twist_controller],
  deactivate_controllers: [joint_trajectory_controller],
  strictness: 1,
  activate_asap: true,
}"
```

Once the twist_controller is activated, You can publish Twist messages on the /twist_controller/commands topic to command the arm.  

For example, you can jog the arm using Teleop Twist Keyboard with the following command:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap /cmd_vel:=/twist_controller/commands
```

If you wish to use the joint_trajectory_controller again to command the arm using JointTrajectory messages, run the following:

```bash
ros2 service call /controller_manager/switch_controller controller_manager_msgs/srv/SwitchController "{
  activate_controllers: [joint_trajectory_controller],
  deactivate_controllers: [twist_controller],
  strictness: 1,
  activate_asap: true,
}"
```

# Forked from Kinovarobotics/ros2_kortex
[refer to original repository](https://github.com/Kinovarobotics/ros2_kortex)