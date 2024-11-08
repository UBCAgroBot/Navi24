import json
import time

import os
import rclpy
from rclpy.node import Node
import threading
from std_msgs.msg import String

import html

# import serial
from flask import Flask, jsonify, request, render_template, redirect

# SERIAL_PORT = "/dev/ttyACM0"

app = Flask(__name__)


class Publisher(Node):
    def __init__(self):
        super().__init__('publisher_node')

        self.publisher_ = self.create_publisher(String, '/publish', 5)

    def publish_motion(self, message):
        msg = String()
        msg.data = message
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')


rclpy.init()
motion_publisher = Publisher()



# def start_serial():
#     global ser
#     ser = serial.Serial(
#         port=SERIAL_PORT,
#         baudrate=9600,
#         # parity=serial.PARITY_NONE,
#         # stopbits=serial.STOPBITS_ONE,
#         # bytesize=serial.EIGHTBITS,
#         timeout=1,
#     )


# start_serial()


@app.route("/")
def hello_world():
    return "<p>This is a robot</p>"


@app.route("/control", methods=["POST"])
def update_record():
    input = json.loads(request.data)
    if not ("speed" in input and input["speed"] >= -128 and input["speed"] <= 127):
        return json.dumps({"error": "Speed missing or out or range"})

    if not (
        "direction" in input and input["direction"] >= -30 and input["direction"] <= 30
    ):
        return json.dumps({"error": "Direction missing or out or range"})

    if not (
        "mode" in input
        and (input["mode"] == 0 or input["mode"] == 1 or input["mode"] == 2)
    ):
        return json.dumps({"error": "Mode missing or out or range"})

    direction_out = input["direction"] & 0b00111111
    mode = input["mode"] << 6
    direction_out = direction_out | mode

    out = direction_out.to_bytes(1, "big", signed=True) + input["speed"].to_bytes(
        1, "big", signed=True
    )

    threading.Thread(target=motion_publisher.publish_motion, args=(out.hex(),)).start()

    # ser.write(out + b"\n")
    # time.sleep(0.01)

    print("Sent: ", out)
    print("Got: ", input)

    return json.dumps({"message": "okay"})

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    try:
        threading.Thread(target=run_flask).start()
        
        rclpy.spin(motion_publisher)
    
    except KeyboardInterrupt:
        pass
    finally:
        motion_publisher.destroy_node()
        rclpy.shutdown()
