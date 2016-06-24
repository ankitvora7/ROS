#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
rospy.init_node('keys_to_twist')
keys = {'w': [1,0], 'a': [0,1], 'd': [0,-1], 'x': [-1,0], 's': [0,0]}
def keys_callback(msg, twist_pub):
    vel = keys[msg.data[0]]
    t = Twist()
    t.linear.x = vel[0]
    t.angular.z = vel[1]
    twist_pub.publish(t)
twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=5)
keys_sub = rospy.Subscriber('keys',String,keys_callback,twist_pub)
rospy.spin()
