"""
Uses motor_serial to send instructions directly to 
the Arduino, no ROS.
"""

import argparse
from motor_serial import send_motor_instruction, read_from_arduino

def main():
    parser = argparse.ArgumentParser(description="Send motor direction and speed")
    parser.add_argument(
        'direction',
        type=int,
        help="Direction of the motor [-180 to 180]."
    )
    parser.add_argument(
        'speed',
        type=int,
        help="Speed of the motor [-128 to 127]."
    )

    args = parser.parse_args()
    
    send_motor_instruction(0, args.direction, args.speed)
    print(read_from_arduino())

if __name__ == "__main__":
    main()