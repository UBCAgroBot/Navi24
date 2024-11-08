import rclpy
from rclpy.node import Node
from ros_nav.msg import Motor

class MotorSubscriber(Node):
    def __init__(self):
        super().__init__('motor_subscriber')
        self.subscription = self.create_subscription(
            Motor,
            'motor_instruction',
            self.listener_callback,
            10)
        self.subscription
    
    def listener_callback(self, msg):
        print(f"Speed: {msg.speed}, Direction: {msg.direction}")

def main(args=None):
    rclpy.init(args=args)
    motor_subscriber = MotorSubscriber()
    rclpy.spin(motor_subscriber)
    motor_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
