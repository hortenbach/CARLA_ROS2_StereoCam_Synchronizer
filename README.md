# CARLA_ROS2_StereoCam_Synchronizer
Example for an ROS2 publisher for publishing a corrected CameraInfo.msg for right camera in a CARLA stereo vision setup

## status
code is working but I have not made a clean export for you to use the module out of the box yet. So you might have to build your own package and copy the code. But since this example might help with the initial confusion when setting up a stereo system on carla I leave it here anyways. 

## What
### Stereo Synchronizer 2
Running CARLA Simulator with CARLA-ROS-BRIDGE you can attach any number of RGB camera sensors to your agent, 
but their respective CameraInfo.msg topic is always assuming a mono vision setup.

This publisher is an example on how to overwrite the projection matrix for the right camera of a stereo vision setup, used in stereo odometry.
The according math and explanations can be reviewed in the CameraInfo.msg documentation at:
https://github.com/ros2/common_interfaces/blob/master/sensor_msgs/msg/CameraInfo.msg 
From the CameraInfo.msg source:
```
# Projection/camera matrix
#     [fx'  0  cx' Tx]
# P = [ 0  fy' cy' Ty]
#     [ 0   0   1   0]
# By convention, this matrix specifies the intrinsic (camera) matrix
#  of the processed (rectified) image. That is, the left 3x3 portion
#  is the normal camera intrinsic matrix for the rectified image.
# It projects 3D points in the camera coordinate frame to 2D pixel
#  coordinates using the focal lengths (fx', fy') and principal point
#  (cx', cy') - these may differ from the values in K.
# For monocular cameras, Tx = Ty = 0. Normally, monocular cameras will
#  also have R = the identity and P[1:3,1:3] = K.
# For a stereo pair, the fourth column [Tx Ty 0]' is related to the
#  position of the optical center of the second camera in the first
#  camera's frame. We assume Tz = 0 so both cameras are in the same
#  stereo image plane. The first camera always has Tx = Ty = 0. For
#  the right (second) camera of a horizontal stereo pair, Ty = 0 and
#  Tx = -fx' * B, where B is the baseline between the cameras.
# Given a 3D point [X Y Z]', the projection (x, y) of the point onto
#  the rectified image is given by:
#  [u v w]' = P * [X Y Z 1]'
#         x = u / w
#         y = v / w
#  This holds for both images of a stereo pair.
float64[12] p # 3x4 row-major matrix
```

Note: Since we are using the simulated CARLA sensors we do not have to deal with distortion, therefor no camera calibration is needed either. 
So you will find P = K|t in this case, since tx = tx' ty=ty' cx=cx' cy=cy'


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
