#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge
class Follower:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window",1)
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image,self.image_callback)

    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
        cv2.imshow("window",image)
        cv2.waitKey(300)


if __name__ == '__main__':
    rospy.init_node('follower_opencv')
    follower = Follower()
    rospy.spin()
