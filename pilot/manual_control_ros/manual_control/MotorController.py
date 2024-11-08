import rclpy
import time
from std_msgs.msg import Float64
from rclpy.node import Node
import serial

SERIAL_PORT = "/dev/ttyACM0"


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

        self.speed = 0
        self.direction = 0
        self.ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=9600,
            timeout=1,
        )

    def speed_callback(self, msg):
        print(f'Received - Speed: {msg.data}')
        self.speed = msg.data
        self.send_data()

    def direction_callback(self, msg):
        self.direction = msg.data
        print(f'received - Direction {msg.data}')
        self.send_data()

    def send_data(self):
        direction_out = int(self.direction) & 0b00111111
        mode = 0 << 6
        direction_out = direction_out | mode

        out = direction_out.to_bytes(1, "big", signed=True) + int(self.speed).to_bytes(
            1, "big", signed=True
        )

        self.ser.write(out + b"\n")
        # time.sleep(0.01)
        # print(message)
        #print(self.ser.readall())


def main(args=None):
    rclpy.init(args=args)
    motor_controller_node = MotorControllerNode()
    rclpy.spin(motor_controller_node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
