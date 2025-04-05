import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from nav_workspace.src.ros_nav.ros_nav.utils.edge_algorithm import detect_edges

class EdgeDection(Node):
    def __init__(self):
        super().__init__('edge_detection')
        
        # Publish processed image with edge detection every second
        self.publisher_ = self.create_publisher(Image, 'edge_detect', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Subscriber to get image data
        self.img_subscription = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw', # Place holder
            self.img_callback,
            10)

        self.img_subscription
        self.edges_frame = None
        self.bridge = CvBridge()


    def img_callback(self, img_msg):
        # Convert ROS image to OpenCV image
        image = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding='bgr8')
        cv_image = detect_edges(image)

        # Convert OpenCV image to a grayscale ROS image
        self.edges_frame = self.bridge.cv2_to_imgmsg(cv_image, encoding='mono8')

    def timer_callback(self):
        if self.edges_frame:
            self.publisher_.publish(self.edges_frame)
            self.get_logger().info("Published image with edge detection")
        

def main(args=None):
    rclpy.init(args=args)

    edge_detection = EdgeDection()

    rclpy.spin(edge_detection)
    edge_detection.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

