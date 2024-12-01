"""
This module provides 2 functions. send_motor_instruction and convert 
"""

import time
import serial

POTENTIAL_SERIAL_PORTS = ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/cu.usbmodem1101"]

serial_conn = None
for SERIAL_PORT in POTENTIAL_SERIAL_PORTS:
    try:
        serial_conn = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None)
        print("Using port: ", SERIAL_PORT)
        break
    except serial.SerialException:
        continue
if serial_conn == None:
    print("Did not connect to any serial ports")

time.sleep(2)

def send_motor_instruction(mode: int, direction:int, speed:int ):

    if (mode > 2):
        raise ValueError("Invalid mode")

    if (speed > 127 or speed < -128):
        raise ValueError("Invalid speed")

    if (direction > 127 or direction < -128):
        raise ValueError("Invalid direction")

    # We want to map [-127, -1] to [191, 255]
    # We want to map [0, 127] to [0, 63]
    # -127 SHOULD BE MAPPED TO ALL ZERO's
    # 127 SHOULD BE MAPPED TO ALL ONCES
    converted_direction = None
    if (direction < 0):
        converted_direction =  int(191 + (direction + 127) * 64 / 126)
    else:
        converted_direction = int(direction * 63 / 127)

    speed = max(min(speed, 100), -100)

    if serial_conn == None:
        print("No serial connection, skipping write")
        return
        
    output = mode.to_bytes(1, 'little', signed=True) + \
            converted_direction.to_bytes(1, 'little', signed=False) + \
            speed.to_bytes(1, 'little', signed=True)
    serial_conn.write(output)


def read_from_arduino():

    try:
        if serial_conn:
            response = serial_conn.read_until()
            print(response.decode('utf-8'))
        else:
            print("No serial connection, skipping read")

    except Exception as e:
        print(f"Error reading from serial: {e}")

def connected_to_serial():
    if serial_conn is not None:
        return True
    else:
        return False