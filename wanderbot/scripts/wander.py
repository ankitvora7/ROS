#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import roslib
rospy.init_node('wander')
def scan_callback(msg):
    global range_ahead
    range_ahead = msg.ranges[len(msg.ranges)/2]
range_ahead = 1
scan_sub = rospy.Subscriber('scan',LaserScan,scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size=5)
cmd_vel = Twist()
cmd_vel.linear.x = 0.5
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    while range_ahead > 0.8:
        cmd_vel.angular.z = 0.0
        cmd_vel.linear.x = 0.5
        cmd_vel_pub.publish(cmd_vel)
    cmd_vel.linear.x = 0.0
    cmd_vel.angular.z = 0.15
    cmd_vel_pub.publish(cmd_vel)
    rate.sleep()
