#!/usr/bin/env python
import rospy
import numpy as np
from common_msgs.msg import Float32Vector3
from common_msgs.srv import service, serviceResponse


def service_callback(request):
    response = serviceResponse(sum=np.sqrt(request.vectorx**2+request.vectory**2+request.vectorz*2))
    print "reset"
    return response

def callback(msg):
    vectorx=msg.vector3.x*msg.data
    vectory=msg.vector3.y*msg.data
    vectorz=msg.vector3.z*msg.data
    sumvector=np.sqrt(vectorx**2+vectory**2+vectorz**2)
    print "float * vector:\n    msg.vector3.x : %f\n    msg.vector3.y : %f\n    msg.vector3.z : %f\n    sumvector : %f" %( vectorx, vectory, vectorz ,sumvector)

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('merge_msg', Float32Vector3, callback)
service = rospy.Service('merge',service, service_callback)
rospy.spin()
