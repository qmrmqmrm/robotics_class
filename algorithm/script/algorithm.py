#!/usr/bin/env python
import rospy
from common_msgs.msg import Float32Vector3
from std_msgs.msg import String

def callback(msg):
    print "msg.data : %f msg.vector3.x : %f, msg.vector3.y: %f, msg.vector3.z : %f" %(msg.data, msg.vector3.x, msg.vector3.y, msg.vector3.z)

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('merge_msg', Float32Vector3, callback)
rospy.spin()
