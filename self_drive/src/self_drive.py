#! /home/j/.pyenv/versions/ros_py365/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher
        self.turtle_vel = Twist()
        self.rate = 10
        self.count = 0
        
    def average(self,a):
        avg = 0
        sum_ = 0
        count_ = 0
        for num in a:
            if num != 0:
                sum_ = sum_ + num
                count_ = count_ + 1
                
        try :
            avg = sum_ / count_
        except ZeroDivisionError:
            pass
            
        return avg
        
        
        
    def lds_callback(self, scan):
        avg_left = self.average(scan.ranges[270:300])
        avg_right = self.average(scan.ranges[240:269])
        avg_follow =self.average(scan.ranges[240:300])
        gap = avg_left - avg_right
        avg_foward = self.average(scan.ranges[350:359])
        if gap > 0.05 :
            gap = 0.05

        elif gap <-0.05 :
            gap = -0.05

        if avg_foward <= 0.4 and avg_foward != 0:
            self.goturn(1,2.5)

        elif avg_follow <= 0.35 and avg_follow != 0:
            self.goturn(1,-gap*20)

        else :
            if avg_right <= 0.35 and avg_right != 0:
                self.goturn(0,-2)

            elif avg_right >0.35 and avg_left < 0.35:
                self.goturn(1,-0.95)

            else :
                self.goturn(1,0)

    def goturn(self,x,z):
    
        self.turtle_vel.linear.x = 0.22
        self.turtle_vel.angular.z = z
        #print(a*4)
        self.publisher.publish(self.turtle_vel)

def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    driver.rate = rospy.Rate(3.8)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
    
    
