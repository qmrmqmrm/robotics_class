#!/usr/bin/env python
import rospy
from common_msgs.msg import Float32Vector3

rospy.init_node('Sensor_Pub')
pub = rospy.Publisher('merge_msg',Float32Vector3,queue_size=1)
msg = Float32Vector3()
rate = rospy.Rate(1)
msg.data = 0
msg.vector3.x = 0
msg.vector3.y = 0
msg.vector3.z = 0
while not rospy.is_shutdown():
    msg.data += 1
    for a in range(msg.data):
        msg.vector3.x +=1
        msg.vector3.y +=a
        msg.vector3.z -=a
    print "msg.data : %f msg.vector3.x : %f, msg.vector3.y: %f, msg.vector3.z : %f" %(msg.data, msg.vector3.x, msg.vector3.y, msg.vector3.z)
    pub.publish(msg)
    rate.sleep()
