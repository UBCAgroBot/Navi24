"""
This module provides 2 functions. send_motor_instruction and convert 
"""

import time
import serial

# SERIAL_PORT = "/dev/cu.usbmodem1101"
SERIAL_PORT = "/dev/ttyACM0"

serial_conn = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None)
time.sleep(2)

def send_motor_instruction(mode: int, direction:int, speed:int ):
    if (mode > 2):
        raise ValueError("Invalid mode")

    if (speed > 127 or speed < -128):
        raise ValueError("Invalid speed")

    if (direction > 127 or direction < -128):
        raise ValueError("Invalid direction")

    output = mode.to_bytes(1, 'little', signed=True) + \
            speed.to_bytes(1, 'little', signed=True) + \
            direction.to_bytes(1, 'little', signed=True)
    serial_conn.write(output)

    read_from_arduino()

def read_from_arduino():

    try:
        response = serial_conn.read_until()
        print(response.decode('utf-8'))

    except Exception as e:
        print(f"Error reading from serial: {e}")
