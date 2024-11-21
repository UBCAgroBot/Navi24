"""
This module provides 2 functions. send_motor_instruction and convert 
"""

import time
import serial

# SERIAL_PORT = "/dev/cu.usbmodem1101"
SERIAL_PORT = "/dev/ttyACM0"

serial_conn = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None)

def send_motor_instruction(mode: int, speed: int, direction: int):
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

    print(f"Sent: {mode} , {speed}, {direction}")

def read_from_arduino():

    try:
        response = serial_conn.read_until()
        print(response.decode('utf-8'))

    except Exception as e:
        print(f"Error reading from serial: {e}")

def int_to_str_bits(num, bits):
    if num < 0:
        num = (1 << bits) + num
    elif num >= (1 << bits):
        raise ValueError("More bits than expected")
    
    binary_str = format(num, f'0{bits}b')
    return binary_str
