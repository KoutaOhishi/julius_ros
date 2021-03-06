#!/usr/bin/env python
#encoding: utf8
import rospy, os, socket, sys
from std_msgs.msg import String

class JuliusReceiver:
	def __init__(self): 
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			try:
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect(("localhost", 10500))
				break
			except:
				rate.sleep()

		rospy.on_shutdown(self.sock.close)

	def get_line(self):
		line =""
		while not rospy.is_shutdown():
			v = self.sock.recv(1)
			if v == '\n':
				return line
			line += v
	
	
	def get_word(self):
		line = self.get_line()
		if "WHYPO WORD" in line:
			word = line.split('<WHYPO WORD="')[-1].split('"')[0]
			if word.find('<') == -1:
				return word

 
if __name__ == '__main__':
	rospy.init_node("julius_publisher")
	j = JuliusReceiver()
	word = ""
	while not rospy.is_shutdown():
		pub = rospy.Publisher('/recognition_word', String, queue_size=100)
		r = rospy.Rate(1)
		recog_word = j.get_word()
		if recog_word != None:
			word += recog_word
			print '[{0}]'.format(word)
			
		if recog_word == '。': #句点「。」が認識されるまで、文字列を格納する
			pub.publish(String(word))
			print '[{0}]←Published'.format(word)
			word = ""
			r.sleep()

		
