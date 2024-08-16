class Sensor:
    """ Base class to implement sensor interfaces """

    def __init__(self):
        print("CALLING A FUNCTION THAT IS NOT IMPLEMENTED: sensor.__init__()")
        pass

    def latest(self):
        """ Pull the latest available data from the sensor. A sensor might be
            implemented such that it captures data from the device when this
            function is called, or it can be implemented such that it captures
            data periodically and returns the latest available capture. Hence,
            returning a UNIX timestamp is required with the sensor data.

        Params:
            none
 
        Returns:
            Object, int: latest available data and its timestamp
        """
        print("CALLING A FUNCTION THAT IS NOT IMPLEMENTED: Sensor.latest()")
        return None, 0
