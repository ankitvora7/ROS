#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
rospy.init_node('keys_to_twist_with_rate')
keys = {'w': [1,0], 'a': [0,1], 'd': [0,-1], 'x': [-1,0], 's': [0,0]}

def keys_callback(msg, twist_pub):
    print 'In the callback'
    vel = keys[msg.data[0]]
    g_last_twist.linear.x = vel[0]
    g_last_twist.angular.z = vel[1]
    twist_pub.publish(g_last_twist)
if __name__=='__main__':
    global g_last_twist
    print 'Running main'
    twist_pub = rospy.Publisher('cmd_vel',Twist,queue_size=5)
    keys_sub = rospy.Subscriber('keys',String,keys_callback,twist_pub)
    rate = rospy.Rate(10)
    g_last_twist = Twist()
    while not rospy.is_shutdown():
        twist_pub.publish(g_last_twist)
        rate.sleep()
