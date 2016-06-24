#!/usr/bin/env python
import rospy,cv2,cv_bridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
import numpy as np

class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window",1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image,self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size=10)
        self.twist = Twist()

    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        imagehsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        lower_yel = np.array([20, 20, 170])
        upper_yel = np.array([255, 255, 190])
        mask = cv2.inRange(imagehsv,lower_yel,upper_yel)
        h,w,d = imagehsv.shape
        top = np.floor(0.75*h)
        bottom = top + 20
        mask[0:top,0:w] = 0
        mask[bottom:h,0:w] = 0
        M = cv2.moments(mask)
        if M['m00']>0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image,(cx,cy),20,(0,0,255),-1)
            err = cx - w/2
            kp = 0.01
            self.twist.linear.x = 0.2
            self.twist.angular.z = -kp*float(err)
            print self.twist.angular.z
            self.cmd_vel_pub.publish(self.twist)
        cv2.imshow("window",image)
        cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('follower_opencv')
    follower = Follower()
    rospy.spin()
