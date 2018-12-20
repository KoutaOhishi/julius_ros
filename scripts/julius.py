#!/usr/bin/env python
import rospy, os

def kill():
	os.system("kill all julius")

os.chdir("/home/ohishikouta/julius-kits/dictation-kit-v4.3.1-linux")
#rospy.init_node("julius")
#rospy.on_shutdown(kill)
os.system("julius -C main.jconf -C am-gmm.jconf -demo -input mic -module")

rospy.spin()
