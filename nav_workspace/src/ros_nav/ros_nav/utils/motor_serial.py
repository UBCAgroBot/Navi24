import time
import serial

SERIAL_PORT = "/dev/cu.usbmodem1101"

def send_bits(mode:str, direction:str, speed:str):
    """
    Writes 16bits to the arduino. The 16 bits should follow 
    the protocol in the Navi24 document. Note the bits are 
    passed as a string.

    Example:
        send_bits("1110011111111111")
    """
    if len(mode) != 2 and all(bit in '01' for bit in mode):
        raise ValueError("Mode must be 2 bits and consist of 0 & 1's")
    if len(direction) != 6 and all (bit in '01' for bit in direction):
        raise ValueError("Direction must be 6 bits and consist of 0's & 1's")
    if len(speed) != 8 and all (bit in '01' for bit in speed):
        raise ValueError("Speed must be 8 bits and consist of 0's & 1's")
    
    if mode == '11':
        raise ValueError("Mode 3,'11' is undefined")
    # There are 3 invalid direction values, -32, -31, and 31
    if direction == '100000':
        raise ValueError("-32 is an invalid direction")
    if direction == '100001':
        raise ValueError("-31 is an invalid direction")
    if direction == '011111':
        raise ValueError("31 is an invalid direction")

    serial_conn = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None )
    time.sleep(2)
    message = str(mode + direction + speed)
    out = (message + '\n').encode('utf-8')
    serial_conn.write(out)
    
    # For testing read the next 2 bits sent back.
    response = serial_conn.read_until()
    print("Raw Arduino response:", response.decode('utf-8'))
    serial_conn.close()
