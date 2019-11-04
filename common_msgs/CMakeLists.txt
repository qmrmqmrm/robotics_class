cmake_minimum_required(VERSION 2.8.3)
project(common_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Float32Vector3.msg
 )
add_service_files(
  FILES
  service.srv
)
generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)


catkin_package(

  LIBRARIES common_msgs
  CATKIN_DEPENDS geometry_msgs rospy std_msgs

)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


