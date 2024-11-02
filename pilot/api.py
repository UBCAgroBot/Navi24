import json
import time

import serial
from flask import Flask, jsonify, request
from flask_cors import CORS

SERIAL_PORT = "/dev/ttyACM0"

app = Flask(__name__)
CORS(app)


def start_serial():
    global ser
    ser = serial.Serial(
        port=SERIAL_PORT,
        baudrate=9600,
        # parity=serial.PARITY_NONE,
        # stopbits=serial.STOPBITS_ONE,
        # bytesize=serial.EIGHTBITS,
        timeout=1,
    )


start_serial()


@app.route("/")
def hello_world():
    return "<p>This is a robot</p>"


@app.route("/control", methods=["POST"])
def update_record():
    input = json.loads(request.data)
    input["speed"] = int(round(input["speed"]))
    input["direction"] = int(round(input["direction"]))
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

    ser.write(out + b"\n")
    time.sleep(0.01)
    print("Sent: ", out)
    print("Got: ", input)

    return json.dumps({"message": "okay"})
