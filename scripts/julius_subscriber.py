#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	print 'recognized word is [{0}]'.format(data.data)	

def julius_subscriber():
	rospy.init_node('julius_subscriber', anonymous=True)
	rospy.Subscriber("/recognition_word", String, callback)
	rospy.spin()

if __name__ == '__main__':
	julius_subscriber()
