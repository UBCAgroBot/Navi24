import rclpy
from rclpy.node import Node
from interfaces.msg import Motor
from ros_nav.utils.motor_serial import send_bits

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(
            Motor,
            'motor_instruction',
            self.listener_callback,
            10)
        self.subscription
    
    def listener_callback(self, msg):
        print(f"Speed: {msg.speed}, Direction: {msg.direction}, Mode: {msg.mode}")

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
