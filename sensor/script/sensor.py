#!/usr/bin/env python
import rospy
from common_msgs.msg import Float32Vector3
from common_msgs.srv import service, serviceRequest


rospy.init_node('Sensor_Pub')
pub = rospy.Publisher('merge_msg',Float32Vector3,queue_size=1)
rospy.wait_for_service('merge')
requester=rospy.ServiceProxy('merge',service)

msg = Float32Vector3()
rate = rospy.Rate(1)

while not rospy.is_shutdown():
   
    
        
    msg.data = 0
    msg.vector3.x = 0
    msg.vector3.y = 0
    msg.vector3.z = 0

    while msg.data <24:
        msg.data += 1
        msg.vector3.x +=2
        msg.vector3.y +=3
        msg.vector3.z +=4
        if msg.data % 24 == 0:
            req = serviceRequest(vectorx=msg.vector3.x, vectory=msg.vector3.y, vectorz=msg.vector3.z)
            res = requester(req)
            print "response:", res.sum, " and reset"
        print "float32\n    msg.data :",msg.data,"\nvector3\n    msg.vector3.x :",msg.vector3.x,"\n    msg.vector3.y :",msg.vector3.y,"\n    msg.vector3.z :",msg.vector3.z
        pub.publish(msg)
        rate.sleep()
            
            
            
            
