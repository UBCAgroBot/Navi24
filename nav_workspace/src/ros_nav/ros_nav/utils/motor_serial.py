import time
import serial

SERIAL_PORT = "/dev/cu.usbmodem101"

serial = serial.Serial(
    port=SERIAL_PORT,
    baudrate=9600,
    timeout=1
)

message = 0b1111111111111111
out = message.to_bytes(2, "big", signed=False)
print("Sending:", out)
serial.write(out + b"\n")

# Read each byte that Arduino sends back until we receive 2 bytes.
response = serial.read(2)  # Expecting 2 bytes back
print("Raw Arduino response:", response)

serial.close()