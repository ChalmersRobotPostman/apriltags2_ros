#!/usr/bin/env python

# A subscriber as well as a publisher to implement some functions according to the given QR code messages.

import rospy
import sys
import numpy as np
import time
from tf.transformations import euler_from_quaternion
#from geometry_msgs.msg import Twist,Point
import math
#from nav_msgs.msg import Odometry
from std_msgs.msg import String
from apriltags2_ros.msg import AprilTagDetectionArray
 

def ccallback(msg):
    global received
    global Msg
    received = msg.detections
    Msg = msg


def QRfunction():
    global received
    global Msg
    pub = rospy.Publisher('QRcode', String, queue_size=10)
    rospy.init_node("attest", anonymous=True)
    sub = rospy.Subscriber("/tag_detections", AprilTagDetectionArray, ccallback)
    rate_g = rospy.Rate(30)
    rate_sub = rospy.Rate(1)

    while not rospy.is_shutdown():
        global flag
      #rospy.loginfo('received='.format(received))
        if received==[] and flag == 0: # the robot doesn't detect anything
            pub_mess = 'searching tags'
            rospy.loginfo(pub_mess)
            pub.publish(pub_mess)
            rate_sub.sleep()
         #rospy.loginfo('Searching')

        elif received[0].id[0]==10 and flag == 0: # 10: the tag outside the elevator 
            pub_mess = 'elevator'
            rospy.loginfo(pub_mess)
            pub.publish(pub_mess)
            rate_sub.sleep()
      
        elif received[0].id[0]==20 and flag == 0: # 20: robot will go and stay inside the elevator
            pub_mess = 'five'
            rospy.loginfo(pub_mess)
            pub.publish(pub_mess)
            rate_sub.sleep()

        elif received[0].id[0]==01 and flag == 0: # 1: robot will go outside the elevator
            pub_mess = 'elevatortwo'
            rospy.loginfo(pub_mess)
            pub.publish(pub_mess)
            rate_sub.sleep()

	elif received[0].id[0]==40 and flag == 0: # 40: robot will go outside the elevator
            pub_mess = 'gf'
            rospy.loginfo(pub_mess)
            pub.publish(pub_mess)
            rate_sub.sleep()

        rate_g.sleep()

# main code
if __name__ == '__main__':
    try:
        received = []
        Msg = []
        flag = 0
        QRfunction()
    except rospy.ROSInterruptException:
        pass
