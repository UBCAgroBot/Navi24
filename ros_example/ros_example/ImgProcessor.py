from std_msgs.msg import Float64
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class ImageProcessor(Node):

    def __init__(self):
        super().__init__('image_processor')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image',
            self.callback,
            10
        )
        self.speed_publisher_ = self.create_publisher(Float64, 'speed', 10)
        self.direction_publisher_ = self.create_publisher(Float64, 'direction', 10)
        self.bridge = CvBridge()

    def callback(self, msg):
        print(f"received {msg.height} x {msg.width} image")
        speed_msg = Float64()
        speed_msg.data = 42.0
        self.speed_publisher_.publish(speed_msg)
        direction_msg = Float64()
        direction_msg.data = 180.0
        self.direction_publisher_.publish(direction_msg)

        print(f"Published speed: {speed_msg.data}, direction: {direction_msg.data}")


def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    image_processor.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
