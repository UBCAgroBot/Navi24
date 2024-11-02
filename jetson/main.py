from sensors import Lidar, ColorCamera, DepthCamera
from motors import Drive
import time
import cv2
import matplotlib.pyplot as plt

DEBUG = True


def main():
    """ Starting point of the robot software

    Params:
        none

    Returns:
        none
    """
    lidar = Lidar()
    cam = ColorCamera(0)
    dcam = DepthCamera()
    d = Drive()

    theta = []
    r = []

    while True:
        l_data, l_time = lidar.latest()
        c_frame, c_time = cam.latest()
        d_frame, d_time = dcam.latest()

        # Driving algorithm

        d.drive(1, 0)

        if DEBUG:
            print("Latest LIDAR reading:", l_data)
            print("Latest camera reading", int(time.time() - c_time), "seconds ago")
            
            #cv2.imshow('a', c_frame)
            #cv2.waitKey(5000)
        

if __name__ == "__main__":
    main()
