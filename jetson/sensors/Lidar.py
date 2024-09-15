from .Sensor import Sensor
from rplidar import RPLidar
import time
import threading


class Lidar(Sensor):
    def __init__(self):
        super()
        self.lidar = RPLidar('/dev/ttyUSB0')
        self.scan = 0
        self.ts = 0
        print("LIDAR INFO:", self.lidar.get_info())
        print("LIDAR HEALTH:", self.lidar.get_health())
        self.t = threading.Thread(target=self.task, name='lidar_task')
        self.t.start()

    def task(self):
        for scan in self.lidar.iter_scans():
            self.scan = scan
            self.ts = time.time()

    def latest(self):
        return self.scan, self.ts
