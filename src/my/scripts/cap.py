#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Sub_Img_Data:
    def __init__(self):
        self.capNum=36
        self.bridge = CvBridge()
        rospy.init_node("camera_node")
        rospy.Subscriber("/oak/rgb/image_raw", Image, self.camera_CB)

    def camera_CB(self, data):

        img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
        cv2.imshow("img", img)

        if cv2.waitKey(1) == ord("q"):
            cv2.imwrite('/home/tony/catkin_ws/src/my/images/%d.png'%self.capNum, img)
            self.capNum += 1

if __name__ == "__main__":
    sub_img_data = Sub_Img_Data()
    rospy.spin()