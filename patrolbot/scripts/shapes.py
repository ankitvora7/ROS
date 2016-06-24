#!/usr/bin/env python
import rospy
from smach import State, StateMachine
from time import sleep
class Drive(State):
    def __init__(self,distance):
        State.__init__(self,outcomes=['success'])
        self.distance = distance
    def execute(self,userdata):
        print "Driving",self.distance
        sleep(3)
        return 'success'
class Turn(State):
    def __init__(self,angle):
        State.__init__(self,outcomes=['success'])
        self.angle = angle
    def execute(self,userdata):
        print "Turning",self.angle
        sleep(3)
        return 'success'
def poly(sides):
    poly = StateMachine(outcomes=['success'])
    for i in range(0,sides-1):
        StateMachine.add('SIDE{0}'.format(i+1),Drive(1),transitions={'success':'TURN{0}'.format(i+1)})
        StateMachine.add('TURN{0}'.format(i+1),Turn(360.0/sides),transitions={'success':'SIDE{0}'.format(i+2)})
    StateMachine.add('SIDE3',Drive(1),transitions={'success':'success'})
    return poly
if __name__ == '__main__':
    rospy.init_node('shapes')
    triangle = poly(3)
    square = poly(4)
    shapes = StateMachine(outcomes=['success'])
    with shapes:
        StateMachine.add('SQUARE',square,transitions={'success':'TRIANGLE'})
        StateMachine.add('TRIANGLE',triangle,transitions={'success':'success'})

    shapes.execute()
