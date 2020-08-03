cmake_minimum_required(VERSION 2.8.3)
project(self_drive)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  sensor_msgs
  std_msgs
)

catkin_package(

  CATKIN_DEPENDS geometry_msgs roscpp sensor_msgs std_msgs

)

