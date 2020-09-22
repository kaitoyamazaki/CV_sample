#!/usr/bin/env python3

import rospy
import cv2
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Image_processing(object):
    def __init__(self):
        self.img_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)
        self.bridge = CvBridge()

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
            cv2.imshow("origin", cv_image)
            cv2.imshow("hsv", hsv)
            
            cv2.waitKey(1)
        except CvBridgeError as e:
            print(e)


if __name__ == "__main__":
    rospy.init_node("image")
    Img = Image_processing()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
