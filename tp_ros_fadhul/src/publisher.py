#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import math
def main():
	rospy.init_node("my_PoseStamped")
	pub=rospy.Publisher("my_PoseStamped_publisher",PoseStamped, queue_size=1)
	r=rospy.Rate(20)


	msg = PoseStamped()
	x=2
        y=4
	z=0
	msg.header.frame_id="map"
	while not rospy.is_shutdown():
		msg.pose.position.x=+2
		msg.pose.position.y=4
		msg.pose.position.z=0
                
            
		pub.publish(msg)
		r.sleep()

if __name__ == "__main__":
    try:
    	main()
    except rospy.ROSInterruptException:
    	pass
