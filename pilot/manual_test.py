#! /usr/bin/python3

import glob
import os

import serial
from evdev import InputDevice, ecodes

"""
Gamepad part taken from Nick as answer on StackOverflow
https://stackoverflow.com/questions/44934309/how-to-access-the-joysticks-of-a-gamepad-using-python-evdev
"""

CENTER_TOLERANCE = 350
STICK_MAX = 65536

axis = {
    ecodes.ABS_X: "ls_x",  # 0 - 65,536   the middle is 32768
    ecodes.ABS_Y: "ls_y",
    ecodes.ABS_RX: "rs_x",
    ecodes.ABS_RY: "rs_y",
    ecodes.ABS_BRAKE: "lt",  # 0 - 1023
    ecodes.ABS_GAS: "rt",
    ecodes.ABS_HAT0X: "dpad_x",  # -1 - 1
    ecodes.ABS_HAT0Y: "dpad_y",
    2: "trigger1",
    5: "trigger2",
}

center = {
    "ls_x": STICK_MAX / 2,
    "ls_y": STICK_MAX / 2,
    "rs_x": STICK_MAX / 2,
    "rs_y": STICK_MAX / 2,
}

last = {
    "ls_x": STICK_MAX / 2,
    "ls_y": STICK_MAX / 2,
    "rs_x": STICK_MAX / 2,
    "rs_y": STICK_MAX / 2,
}

"""ser = serial.Serial(
    port="/dev/ttyACM0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)"""


def make_signal(direction, speed, mode):
    """
    direction: between 0 and 65536 where 32768 is the middle
    speed: between 0 and 65536 where 32768 is the middle
    mode: 2 bits which specifies the mode

    Outputs a byte string such that the first 2 bits are the mode,
    the next 6 bits are the signed direction (-30 to 30), the last
    8 bits are the signed speed from (-127 to 127)
    """
    """message = bytes(
        str(5 + int(10 * direction / STICK_MAX))
        + str(5 + int(10 * speed / STICK_MAX))
        + "\n",
        "utf-8",
    )"""

    speed_out = int((speed - (STICK_MAX / 2)) / (STICK_MAX / 2) * 127)
    direction_out = int((direction - (STICK_MAX / 2)) / (STICK_MAX / 2) * 30)

    direction_out = direction_out & 0b00111111
    mode = mode << 6
    direction_out = direction_out | mode

    out = direction_out.to_bytes(1, signed=False) + speed_out.to_bytes(1, signed=True)
    return out


def teleop(event_path=""):

    event_dir = "/dev/input/"

    if event_path == "":
        os.chdir("/dev/input")
        for file in sorted(glob.glob("event20")):
            print(file)  # TEST
            event_path = file

    print(event_dir + event_path)
    device = InputDevice(event_dir + event_path)

    while True:
        for event in device.read_loop():
            if event.type == ecodes.EV_ABS:
                if axis[event.code] in ["ls_y", "rs_x"]:
                    last[axis[event.code]] = event.value

                    value = event.value - center[axis[event.code]]

                    if abs(value) <= CENTER_TOLERANCE:
                        value = 0

                    print(
                        "angle:"
                        + str(last["rs_x"] / STICK_MAX)
                        + " | speed:"
                        + str(last["ls_y"] / STICK_MAX)
                    )

                    message = make_signal(last["rs_x"], last["ls_y"], 0b00)
                    # ser.write(message)
                    print(message)


if __name__ == "__main__":
    teleop()
