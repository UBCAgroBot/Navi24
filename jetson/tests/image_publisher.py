import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher_node')

        self.publisher_ = self.create_publisher(Image, '/camera/image', 10)
        self.timer = self.create_timer(0.1, self.publish_image)  # 10 Hz
        self.bridge = CvBridge()

    def publish_image(self):
        img = np.zeros((480, 640, 3), dtype=np.uint8)

        img_msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        self.publisher_.publish(img_msg)
        self.get_logger().info('Image published.')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
