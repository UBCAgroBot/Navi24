from .Sensor import Sensor


class DepthCamera(Sensor):
    def __init__(self):
        super()

    def latest(self):
        print("NOT IMPLEMENTED: DepthCamera.latest()")
        return None, 0
