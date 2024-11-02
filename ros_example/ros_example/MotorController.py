import rclpy
from std_msgs.msg import Float64
from rclpy.node import Node


class MotorControllerNode(Node):
    def __init__(self):

        super().__init__('motor_controller_node')
        self.speed_subscription = self.create_subscription(
            Float64,
            'speed',
            self.speed_callback,
            10
        )
        self.direction_subscription = self.create_subscription(
            Float64,
            'direction',
            self.direction_callback,
            10
        )

    def speed_callback(self, msg):
        print(f'Received - Speed: {msg.data}')

    def direction_callback(self, msg):
        print(f'received - Direction {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    motor_controller_node = MotorControllerNode()
    rclpy.spin(motor_controller_node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
