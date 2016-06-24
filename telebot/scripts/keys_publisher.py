#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys,select,tty,termios
if __name__=='__main__':
    key_pub  = rospy.Publisher('keys',String,queue_size=1)
    rospy.init_node('keys_publisher')
    rate = rospy.Rate(100)
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    print 'Publishing keystokes. press Ctrl-C to exit...'
    while not rospy.is_shutdown():
        if select.select([sys.stdin],[],[],0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
termios.tcsetattr(sys.stdin,termios.TCSADRAIN,old_attr)
