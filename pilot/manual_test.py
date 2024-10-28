#! /usr/bin/python3

import argparse
import argparse
import glob
import os
import time

#import evdev
import keyboard
import serial
#from evdev import InputDevice, ecodes
import pygame

from time import sleep
from types import MappingProxyType

"""
Gamepad part taken from Nick as answer on StackOverflow
https://stackoverflow.com/questions/44934309/how-to-access-the-joysticks-of-a-gamepad-using-python-evdev
"""

CENTER_TOLERANCE = 0.05
STICK_MAX = 65536
USE_JOYSTICK = False
SERIAL_PORT = "/dev/ttyACM0"

# axis = {
#     ecodes.ABS_X: "ls_x",  # 0 - 65,536   the middle is 32768
#     ecodes.ABS_Y: "ls_y",
#     ecodes.ABS_RX: "rs_x",
#     ecodes.ABS_RY: "rs_y",
#     ecodes.ABS_BRAKE: "lt",  # 0 - 1023
#     ecodes.ABS_GAS: "rt",
#     ecodes.ABS_HAT0X: "dpad_x",  # -1 - 1
#     ecodes.ABS_HAT0Y: "dpad_y",
#     2: "trigger1",
#     5: "trigger2",
# }

# center = {
#     "ls_x": STICK_MAX / 2,
#     "ls_y": STICK_MAX / 2,
#     "rs_x": STICK_MAX / 2,
#     "rs_y": STICK_MAX / 2,
# }

# last = {
#     "ls_x": STICK_MAX / 2,
#     "ls_y": STICK_MAX / 2,
#     "rs_x": STICK_MAX / 2,
#     "rs_y": STICK_MAX / 2,
# }

class JoystickHandler:


    def __init__(self, controller:pygame.joystick.Joystick):

        # immutable dictionary
        self.__AxisNumbers = MappingProxyType( {"LEFT_X":0, "LEFT_Y":1, "LEFT_TRIGGER":4, "RIGHT_Y":3, "RIGHT_X":2,"RIGHT_TRIGGER":5})

        self.__movement_data:dict[str,float] = {"speed":0, "angle":0}

        self.__deadzone_val:float = 0.05
        self.__controller:pygame.joystick.Joystick = controller

        
    
    def get_joystick_inputs(self):

        for event in pygame.event.get():

            if event.type == pygame.JOYAXISMOTION:

                angle_signal = round(self.axis_to_signal_format(self.__controller.get_axis(self.AxisNumbers["RIGHT_X"])) )
                speed_signal = round(self.axis_to_signal_format(-self.__controller.get_axis(self.AxisNumbers["LEFT_Y"])))

                self.__movement_data["speed"] = self.axis_to_speed(self.__controller.get_axis(self.__AxisNumbers["LEFT_Y"]))
                self.__movement_data["angle"] = self.axis_to_angle(self.__controller.get_axis(self.__AxisNumbers["RIGHT_X"]))


                message = make_signal(angle_signal, speed_signal, 0b00)
                print(message)

    
    def get_axis_numbers(self)->MappingProxyType:
        return self.__AxisNumbers
    

    def axis_to_signal_format(self, axis_signal:float)->float:
        """Turn an axis signal into a bit signal for the make_signal function"""
        return STICK_MAX/2*(axis_signal + 1)
    
    # TODO: Add code to these methods to turn axis values into physical quantities
    def axis_to_speed(self,axis_signal:float)->float:
        return 0

    def axis_to_angle(self,axis_signal:float)->float:
        return 0

    def get_movement_data(self)->dict:
        return None






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

    speed_out = clamp(5,int((speed - (STICK_MAX / 2)) / (STICK_MAX / 2) * 127))
    direction_out = clamp(1,int((direction - (STICK_MAX / 2)) / (STICK_MAX / 2) * 30))

    print("direction_out:", direction_out, "Speed_out:", speed_out)

    direction_out = direction_out & 0b00111111
    mode = mode << 6
    direction_out = direction_out | mode

    out = direction_out.to_bytes(1, "big", signed=True) + speed_out.to_bytes(
        1, "big", signed=True
    )
    out = direction_out.to_bytes(1, "big", signed=True) + speed_out.to_bytes(
        1, "big", signed=True
    )
    return out


def get_keyboard_inputs():
    """
    Reads the inputs from the keyboard and puts
    the result in last["rs_x"] and last["ls_y"]
    """
    global last
def get_keyboard_inputs():
    """
    Reads the inputs from the keyboard and puts
    the result in last["rs_x"] and last["ls_y"]
    """
    global last

    if keyboard.read_key() == "a":
        last["rs_x"] -= 1000
        if last["rs_x"] <= 0:
            last["rs_x"] = 0
    if keyboard.read_key() == "a":
        last["rs_x"] -= 1000
        if last["rs_x"] <= 0:
            last["rs_x"] = 0

    elif keyboard.read_key() == "d":
        last["rs_x"] += 1000
        if last["rs_x"] >= STICK_MAX:
            last["rs_x"] = STICK_MAX
    elif keyboard.read_key() == "d":
        last["rs_x"] += 1000
        if last["rs_x"] >= STICK_MAX:
            last["rs_x"] = STICK_MAX

    if keyboard.read_key() == "s" and keyboard.read_key() == "w":
        last["ls_y"] = STICK_MAX / 2
    if keyboard.read_key() == "s" and keyboard.read_key() == "w":
        last["ls_y"] = STICK_MAX / 2

    elif keyboard.read_key() == "s":
        last["ls_y"] -= 1000
        if last["ls_y"] <= 0:
            last["ls_y"] = 0
    elif keyboard.read_key() == "s":
        last["ls_y"] -= 1000
        if last["ls_y"] <= 0:
            last["ls_y"] = 0

    elif keyboard.read_key() == "w":
        last["ls_y"] += 1000
        if last["ls_y"] >= STICK_MAX:
            last["ls_y"] = STICK_MAX
    elif keyboard.read_key() == "w":
        last["ls_y"] += 1000
        if last["ls_y"] >= STICK_MAX:
            last["ls_y"] = STICK_MAX



def setup_joystick(event_path="")-> pygame.joystick.Joystick:
    global device
    event_dir = "/dev/input/"
    global joystick

    # if event_path == "":
    #     os.chdir("/dev/input")
    #     for file in sorted(glob.glob("event20")):
    #         print(file)  # TEST
    #         event_path = file

    # devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    # for device in devices:
    #     if "Gamepad" in device.name:
    #         event_dir = device.path

    # print(event_dir + event_path)
    # device = InputDevice(event_dir + event_path)

    pygame.init()
    pygame.joystick.init()
    
    # We require a joystick for any of this to function
    try:
        joystick =  pygame.joystick.Joystick(0); 
    except pygame.error:
        print("No joystick found")
        exit()
    else:
        return joystick



def clamp(threshold:int, value:int) -> int:

    """:param threshold: positive """

    print(threshold, value)
    if abs(value) <= threshold:
        return 0
    
    return value
    


# def get_joystick_inputs():


#     for event in pygame.event.get():
#         if event.type == pygame.JOYAXISMOTION:

#             angle_signal = round( STICK_MAX/2 *(joystick.get_axis(AxisNumbers["RIGHT_X"])+1) )
#             speed_signal = round( STICK_MAX/2 * (-joystick.get_axis(AxisNumbers["LEFT_Y"])+ 1) )

            
#             message = make_signal(angle_signal, speed_signal, 0b00)
#             print(message)
                 #ser.write(message + b"\n")
    #             time.sleep(0.01)
            #print(joystick.get_axis(AxisNumbers["RIGHT_X"]))
            #print(joystick.get_axis(AxisNumbers["RIGHT_TRIGGER"]))
                
 
    # global device, last
    # for event in device.read_loop():
    #     if event.type == ecodes.EV_ABS:
    #         if axis[event.code] in ["ls_y", "rs_x"]:
    #             last[axis[event.code]] = event.value + 32768

    #             value = event.value - center[axis[event.code]]

    #             if abs(value) <= CENTER_TOLERANCE:
    #                 value = 0

    #             print("angle:" + str(last["rs_x"]) + " | speed:" + str(last["ls_y"]))

    #             # get_keyboard_inputs()

    #             message = make_signal(last["rs_x"], last["ls_y"], 0b00)
    #             print(message)
    #             ser.write(message + b"\n")
    #             time.sleep(0.01)

    #             print(message)
    #             print(ser.readall())


def teleop(event_path=""):

    # if USE_JOYSTICK:
    #     setup_joystick(event_path)
    controllerStick = JoystickHandler(setup_joystick())

    #start_serial() uncomment this later
    while True:
        controllerStick.get_joystick_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--joystick", help="Enable joystick control", action="store_true"
    )
    parser.add_argument(
        "-p", "--port", default="/dev/ttyACM0", help="increase output verbosity"
    )
    args = parser.parse_args()

    USE_JOYSTICK = args.joystick
    SERIAL_PORT = args.port

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--joystick", help="Enable joystick control", action="store_true"
    )
    parser.add_argument(
        "-p", "--port", default="/dev/ttyACM0", help="increase output verbosity"
    )
    args = parser.parse_args()

    USE_JOYSTICK = args.joystick
    SERIAL_PORT = args.port

    teleop()