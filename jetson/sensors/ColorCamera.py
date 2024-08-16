from .Sensor import Sensor
import cv2
import time


class ColorCamera(Sensor):
    def __init__(self, cam_number):
        self.cam = cv2.VideoCapture(cam_number)
        self.latest_frame = None
        self.latest_timestamp = 0
        super()

    def latest(self):
        ret, frame = self.cam.read()
        if ret:
            self.latest_frame = frame
            self.latest_timestamp = time.time()
        return self.latest_frame, self.latest_timestamp
