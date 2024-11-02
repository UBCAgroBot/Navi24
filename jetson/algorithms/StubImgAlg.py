import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
import cv2

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')
        # self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/camera/image',
            self.callback,
            10
        )

    def callback(self, msg):
        print(f"received {msg.height} x {msg.width} image")
        # try:
        #     # cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        #     # # Your image processing logic here
        #     # cv2.imshow("Image", cv_image)
        #     # cv2.waitKey(1)
        # except Exception as e:
        #     self.get_logger().error(f"Failed to process image: {e}")

def main(args=None):
    rclpy.init(args=args)
    image_processor = ImageProcessor()
    rclpy.spin(image_processor)
    image_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
