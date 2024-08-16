from enum import Enum


class Drive:
    """Communicates with motor controller (Arduino) using the protocol
       specified in Navi24 Product Specifications
    """

    class mode(Enum):
        NORMAL = 0
        CRABWALK = 1
        TURN360 = 2

    def __init__(self):
        pass

    def drive(self, speed, angle, mode=mode.NORMAL):
        print("NOT IMPLEMENTED: Drive.drive() cannot send data to Arduino!")
