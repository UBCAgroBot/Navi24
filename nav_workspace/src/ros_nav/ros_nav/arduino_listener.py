import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
from ros_nav.utils.motor_serial import read_from_arduino, connected_to_serial

class ArduinoListener(Node):
    def __init__(self):
        super().__init__('arduino_listener')
        self.publisher_ = self.create_publisher(
            String, 
            'arduino_data', 
            1)


        if connected_to_serial():
            self.timer_period = 0.001
            self.timer = self.create_timer(self.timer_period, self.read_serial_data)

    def read_serial_data(self):
        
        read_from_arduino()


def main(args=None):
    rclpy.init(args=args)
    listener = ArduinoListener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
