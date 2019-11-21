#! /home/j/.pyenv/versions/ros_py365/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher
        self.turtle_vel = Twist()
        
        
    def average(self,a):
        avg = 0
        sum_ = 0
        count_ = 0
        for num in a:
            if num > 0.02:
                #sprint("dd")
                sum_ = sum_ + num
                count_ = count_ + 1
                
        try :
            avg = sum_ / count_
        except ZeroDivisionError:
            pass
            
        return avg
        
        
        
    def lds_callback(self, scan):
         
        avg_right = self.average(scan.ranges[275:300])
        avg_left = self.average(scan.ranges[240:265])
        print("avg",avg_right,avg_left)
        gap = avg_right - avg_left
        print("gap",gap)
        avg_foward = self.average(scan.ranges[330:359])
        print("forward",avg_foward)
       
        if avg_foward <= 0.5:
            print("dddd")
            self.goturn(1,2)
        elif self.average(scan.ranges[240:300])<0.40:
            self.goturn(1,-gap*20)

        else :
            print("go")
            self.goturn(1,0)
        
        self.publisher.publish(self.turtle_vel)	
		
        
    def goturn(self,x,z):
    
        self.turtle_vel.linear.x = x*0.22
        self.turtle_vel.angular.z = z
        #print(a*4)
        

def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
    
    
