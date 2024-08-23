```bash
sudo apt install python3-colcon-mixin
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default
sudo apt install python3-vcstool
mkdir -p ~/ws_moveit2/src
cd ~/ws_moveit2/src
git clone --branch humble https://github.com/ros-planning/moveit2_tutorials
vcs import < moveit2_tutorials/moveit2_tutorials.repos
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
cd ~/ws_moveit2
colcon build --mixin release
echo 'source ~/ws_moveit2/install/setup.bash' >> ~/.bashrc
source ~/.bashrc
ros2 launch moveit2_tutorials demo.launch.py rviz_config:=panda_moveit_config_demo_empty.rviz
```
