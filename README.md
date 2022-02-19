# CARLA_ROS2_StereoCam_Synchronizer
Example for an ROS2 publisher for publishing a corrected CameraInfo.msg for right camera in a CARLA stereo vision setup

## What
Running CARLA Simulator with CARLA-ROS-BRIDGE you can attach any number of RGB cmara sensors to your agent, 
but their respective CameraInfo.msg topic is always assuming a mono vision setup.

This publisher is an example on how to overwrite the projection matrix for the right camera of a stereo vision setup, used in stereo odometry.
The according math and explanations can be reviewd in the CameraInfo.msg documentation at:
https://github.com/ros2/common_interfaces/blob/master/sensor_msgs/msg/CameraInfo.msg 

## build
I recommend following the build instruction for new packages from the official ros2 docs https://docs.ros.org/en/foxy/Tutorials/Creating-Your-First-ROS2-Package.html
```
ros2 pkg create --build-type ament_python <my_package_name>
```

After you created a wordspace folder, place this repo into src folder and make respective changes in your workspace files. 
```
rosdep install -i --from-path src --rosdistro foxy -y

colcon build --packages-select <package>
```
