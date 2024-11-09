"""
Uses motor_serial to send instructions directly to 
the Arduino, no ROS.
"""

import argparse
from motor_serial import send_motor_instruction

mode_one = "00"
direction_straight = "000000"
direction_left = "100010"
direction_right = "011110"
max_speed = "01111111"
no_speed = "00000000"

def go_forward():
    send_motor_instruction(mode_one, direction_straight, max_speed)

def go_left():
    send_motor_instruction(mode_one, direction_left, max_speed)

def go_right():
    send_motor_instruction(mode_one, direction_right, max_speed)

def go_stop():
    send_motor_instruction(mode_one, direction_straight, no_speed)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Control motor direction")
    parser.add_argument(
        'direction',
        choices=['f', 'l', 'r', 's'],
        help="Specify 's' for straight, 'l' for left, or 'r' for right"
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the appropriate function based on the flag
    if args.direction == 'f':
        go_forward()
    elif args.direction == 'l':
        go_left()
    elif args.direction == 'r':
        go_right()
    elif args.direction == 's':
        go_stop()

if __name__ == "__main__":
    main()