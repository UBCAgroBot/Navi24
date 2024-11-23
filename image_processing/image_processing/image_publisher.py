import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from interfaces.msg import Motor

from image_processing.utils.test_algorithms import run_algorithm

vid_file = f"image_processing/crop.mp4"

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Motor, 'motor_instruction', 10)
        self.timer = self.create_timer(0.03, self.timer_callback)
        self.cap = cv2.VideoCapture(vid_file) 
        self.bridge = CvBridge()
        
        if not self.cap.isOpened():
            self.get_logger().error('Video source could not be opened!')
            raise RuntimeError('Video source error')

    def timer_callback(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warning('No frame received, ending stream...')
            self.cap.release()
            self.destroy_node()
            return
        
        angle = run_algorithm(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            self.destroy_node()
        
        msg = Motor()
        msg.mode = 0
        msg.speed = 10
        msg.direction = int(angle)

        self.publisher_.publish(msg)
        #self.get_logger().info('Published angle.')

def main(args=None):
    rclpy.init(args=args)
    node = VideoPublisher()

    rclpy.spin(node)
    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()
