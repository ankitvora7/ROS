#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
rospy.init_node('range_ahead')
def scan_cb(msg):
    range_ahead = msg.ranges[len(msg.ranges)/2]
    print '[Range Ahead] range ahead : %0.1f'%range_ahead
scan_sub = rospy.Subscriber('scan',LaserScan,scan_cb)
rospy.spin()   
