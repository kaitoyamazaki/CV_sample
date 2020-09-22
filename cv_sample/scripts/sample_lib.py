#!/usr/bin/env python3

import rospy
from cv_sample.image_converter import Image_converter


def main():
    rospy.init_node("image_pro")
    converter = Image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

#Original_author ... Koki Shirota
