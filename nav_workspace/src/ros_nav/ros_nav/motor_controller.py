import rclpy
from rclpy.node import Node
from interfaces.msg import Motor
from ros_nav.utils.motor_serial import send_motor_instruction, SERIAL_NAME, SERIAL_CONN
import time

class MotorController(Node):
    def __init__(self):
        super().__init__('motor')
        self.subscription = self.create_subscription(
            Motor,
            'motor_instruction',
            self.listener_callback,
            1)
        self.subscription

        self.last_msg_time = 0.0
        self.min_interval = 0.08

        self.BACKGROUND_GREEN = "\033[42m"
        self.BACKGROUND_RED = "\033[41m"
        self.BACKGROUND_YELLOW = "\033[43m"
        self.RESET = "\033[0m"
    
    def listener_callback(self, msg):
        # Only allow one msg every 8ms
        current_time = time.time()
        if current_time - self.last_msg_time < self.min_interval:
            return
        self.last_msg_time = current_time

        bg_color = self.BACKGROUND_GREEN
        if not SERIAL_CONN:
            bg_color = self.BACKGROUND_RED

        self.get_logger().info(f"{self.BACKGROUND_YELLOW} MOTOR NODE {self.RESET} mod:{msg.mode}, dir: {msg.direction}, spd: {msg.speed}")
        resp = send_motor_instruction(msg.mode, msg.direction, msg.speed)
        self.get_logger().info(f"{bg_color}{SERIAL_NAME}{self.RESET} {resp}")

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
