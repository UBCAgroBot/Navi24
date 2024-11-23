"""
Uses motor_serial to send instructions directly to 
the Arduino, no ROS.
"""

import argparse
from motor_serial import send_motor_instruction

no_speed = 0
half_speed = 63

def go_forward():
    send_motor_instruction(0, 0, half_speed)

def go_left():
    send_motor_instruction(0, 60, half_speed)

def go_right():
    send_motor_instruction(0, 60, half_speed)

def go_stop():
    send_motor_instruction(0, 0, 0)

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