#!/usr/bin/env python3

import rospy
import roslib
import cv2


def cv_test(cv_img):
    hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
    cv2.imshow("original", cv_img)
    cv2.imshow("hsv", hsv)
    
    cv2.waitKey(1)


if __name__ == "__main__":
    pass

#Original_author ... Koki Shirota
