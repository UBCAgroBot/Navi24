from .Sensor import Sensor


class Lidar(Sensor):
    def __init__(self):
        super()

    def latest(self):
        print("NOT IMPLEMENTED: Lidar.latest()")
        return None, 0
