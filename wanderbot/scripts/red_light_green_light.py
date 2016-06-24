#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import Twist
cmd_vel = rospy.Publisher('cmd_vel',Twist,queue_size=5)
rospy.init_node('red_light_green_light')
red_light = Twist()
green_light = Twist()
green_light.linear.x = 0.5
rate = rospy.Rate(10)
driving_forward = True
light_change_time = rospy.Time.now()
print 'light_change_time :',light_change_time
while not rospy.is_shutdown():
    if driving_forward:
        cmd_vel.publish(green_light)
    else:
        cmd_vel.publish(red_light)
    if light_change_time < rospy.Time.now():
        print 'light_change_time :',light_change_time
        print 'rostime :',rospy.Time.now()
        driving_forward = not driving_forward
        light_change_time = rospy.Time.now() + rospy.Duration(3)
    rate.sleep()
