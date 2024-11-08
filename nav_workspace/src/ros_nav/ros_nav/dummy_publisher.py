import rclpy
from rclpy.node import Node

from ros_nav.msg import Motor


class DummyMotorPublisher(Node):

    def __init__(self):
        super().__init__('dummy_motor_publisher')
        self.publisher_ = self.create_publisher(Motor, 'motor_instruction', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Motor()
        msg.speed = 10
        msg.direction = 5
        msg.mode = 1
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    dummy_motor_publisher = DummyMotorPublisher()
    rclpy.spin(dummy_motor_publisher)

    dummy_motor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()