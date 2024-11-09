import time
import serial

SERIAL_PORT = "/dev/cu.usbmodem101"

def send_bits(bits:str):
    """
    Writes 16bits to the arduino. The 16 bits should follow 
    the protocol in the Navi24 document. Note the bits are 
    passed as a string.
    """
    if not (len(bits) == 16 and all(bit in '01' for bit in bits)):
        raise ValueError("Input must be a 16-bit string of 0's and 1's.")

    serial_conn = serial.Serial(port=SERIAL_PORT, baudrate=9600, timeout=None )
    time.sleep(2)
    out = (bits + '\n').encode('utf-8')
    serial_conn.write(out)
    
    # For testing read the next 2 bits sent back.
    response = serial_conn.read_until()
    print("Raw Arduino response:", response.decode('utf-8'))
    serial_conn.close()


send_bits("1110011100111111")