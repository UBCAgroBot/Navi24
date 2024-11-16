import rclpy
from rclpy.node import Node
from interfaces.msg import Motor
from ros_nav.utils.motor_serial import send_motor_instruction, int_to_str_bits

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(
            Motor,
            'motor_instruction',
            self.listener_callback,
            1)
        self.subscription
    
    def listener_callback(self, msg):
        # print(f"Speed: {msg.speed}, Direction: {msg.direction}, Mode: {msg.mode}")
        spd_str = int_to_str_bits(msg.speed, 8)
        dir_str = int_to_str_bits(msg.direction, 6)
        mode_str = int_to_str_bits(msg.mode, 2)

        send_motor_instruction(mode_str, dir_str, spd_str)


def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
