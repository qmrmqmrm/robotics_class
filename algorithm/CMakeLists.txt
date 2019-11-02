cmake_minimum_required(VERSION 2.8.3)
project(algorithm)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES algorithm
  CATKIN_DEPENDS geometry_msgs rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

