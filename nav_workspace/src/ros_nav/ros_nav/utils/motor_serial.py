import time
import serial

POTENTIAL_SERIAL_PORTS = ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/cu.usbmodem1101"]

SERIAL_CONN = None
SERIAL_NAME = "NO SERIAL CONN"
for SERIAL_PORT in POTENTIAL_SERIAL_PORTS:
    try:
        SERIAL_CONN = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None)
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
        
    output = mode.to_bytes(1, 'little', signed=True) + \
            converted_direction.to_bytes(1, 'little', signed=False) + \
            speed.to_bytes(1, 'little', signed=True)
    
    if not SERIAL_CONN:
        return

    SERIAL_CONN.write(output)


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
