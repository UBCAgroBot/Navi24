import time
import serial

POTENTIAL_SERIAL_PORTS = ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/cu.usbmodem1101"]

TIMEOUT_SECONDS = 2
SERIAL_CONN = None
SERIAL_NAME = " NO ARDUINO "
for SERIAL_PORT in POTENTIAL_SERIAL_PORTS:
    try:
        SERIAL_CONN = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None)
        SERIAL_CONN.timeout = TIMEOUT_SECONDS
        SERIAL_NAME = SERIAL_PORT
        break
    except serial.SerialException:
        continue

time.sleep(2)

def connected_to_serial():
    if SERIAL_CONN is not None:
        return True
    else:
        return False



def send_motor_instruction(mode: int, direction:int, speed:int ):
    """
    Send a motor instruction through the SERIAL_CONN.

    Mode: [0,2] (unused, should be set to 0)
    Direction: [-180, 180] (Direction to point the wheels, 0 is forward)
    Speed: [-128, 127] (How fast to spin the wheels, negative speed means backwards.)
    """

    if (mode > 2):
        raise ValueError("Invalid mode")

    if (speed > 127 or speed < -128):
        raise ValueError("Invalid speed")

    if (direction > 180 or direction < -180):
        raise ValueError("Invalid direction")

    speed = max(min(speed, 100), -100)
        
    output = mode.to_bytes(1, 'little', signed=True) + \
            direction.to_bytes(2, 'little', signed=True) + \
            speed.to_bytes(1, 'little', signed=True)
    
    if not SERIAL_CONN:
        return "not connected through serial"

    SERIAL_CONN.write(output)
    return read_from_arduino()


def read_from_arduino():
    BACKGROUND_GREEN = "\033[42m"
    RESET = "\033[0m"

    if not SERIAL_CONN:
        print("No serial connection, skipping read", flush=True)
        return

    try:
        response = SERIAL_CONN.read_until()
        return response.decode('utf-8')
    except Exception as e:
        print(f"Error reading from serial: {e}", flush=True)
