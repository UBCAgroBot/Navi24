import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
from ros_nav.utils.motor_serial import read_from_arduino, connected_to_serial

class ArduinoListener(Node):
    def __init__(self):
        super().__init__('arduino_listener')
        self.BACKGROUND_GREEN = "\033[42m"
        self.RESET = "\033[0m"

        if connected_to_serial():
            self.timer_period = 0.001
            self.timer = self.create_timer(self.timer_period, self.read_serial_data)

    def read_serial_data(self):
        msg = read_from_arduino()
        self.get_logger().info(f"{self.BACKGROUND_GREEN} {SERIAL_NAME} {self.RESET} {msg}")


def main(args=None):
    rclpy.init(args=args)
    listener = ArduinoListener()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
