#!/usr/bin/env python
import rospy
from common_msgs.msg import Float32Vector3
from std_msgs.msg import String

def callback(msg):
    vectorx=msg.vector3.x*msg.data
    vectory=msg.vector3.y*msg.data
    vectorz=msg.vector3.z*msg.data
    print "float * vector:\n    msg.vector3.x: %f\n    msg.vector3.y: %f\n    msg.vector3.z: %f" %( vectorx, vectory, vectorz)

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('merge_msg', Float32Vector3, callback)
rospy.spin()
