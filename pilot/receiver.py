import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2

class MotionProcessor(Node):
    def __init__(self):
        super().__init__('motion_processor')
        self.subscription = self.create_subscription(
            String,
            '/publish',
            self.callback,
            5
        )

    def callback(self, msg):
        print(f"received {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    motion_processor = MotionProcessor()
    rclpy.spin(motion_processor)
    motion_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()