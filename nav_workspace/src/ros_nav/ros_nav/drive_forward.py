"""
Instead of self driving, this publisher cannot drive. It just sends garbage info...
"""

import rclpy
from rclpy.node import Node
from interfaces.msg import Motor


class DummyMotorPublisher(Node):

    def __init__(self):
        super().__init__('cant_drive')
        self.publisher_ = self.create_publisher(Motor, 'motor_instruction', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Motor()
        msg.speed = 40
        msg.direction = 0
        msg.mode = 1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    dummy_motor_publisher = DummyMotorPublisher()
    rclpy.spin(dummy_motor_publisher)

    dummy_motor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()