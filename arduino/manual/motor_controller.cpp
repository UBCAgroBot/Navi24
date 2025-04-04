#include "motorController.h"
#include "Arduino.h"

// Initialize global variables
WheelDirection wheel_direction = {0, 0, 0, 0};
Command current_command = {0, 0, 0};
const int MAX_ROTATION_ANGLE = 90;

// Define functions
int clamp(int val, int min_val, int max_val) {
    if (val < min_val) return min_val;
    if (val > max_val) return max_val;
    return val;
}

// Helper function to convert bits to a signed integer
int bits_to_int(const int* bits, int num_bits) {
    int value = 0;
    bool is_negative = (bits[0] == 1); // Check if the number is negative (signed bit)

    // Convert bits to integer
    for (int i = 0; i < num_bits; i++) {
        value = (value << 1) | bits[i];
    }

    // If it's a signed number and negative, apply two's complement
    if (is_negative) {
        value -= (1 << num_bits);
    }
    return value;
}

void processCommand(char * receivedBytes) {
  // One char should equal one int8_t
  current_command.mode = receivedBytes[0];
  uint8_t lowByte = static_cast<uint8_t>(receivedBytes[1]); // Least significant byte
  uint8_t highByte = static_cast<uint8_t>(receivedBytes[2]); // Most significant byte
  current_command.direction = static_cast<int16_t>(lowByte | (highByte << 8));
  current_command.speed = receivedBytes[3];

  Serial.print("Mode: ");
  Serial.print(current_command.mode);
  Serial.print(", Direction: ");
  Serial.print(current_command.direction);
  Serial.print(", Speed: ");
  Serial.print(current_command.speed);
  Serial.println();

  calculateWheelDirections();

}

int calculateWheelDirections() {
    float direction = current_command.direction;
    switch (current_command.mode) {
        case 0b01:
            wheel_direction.rear_right = direction;
            wheel_direction.rear_left = direction;
        default:
            wheel_direction.front_right = direction;
            wheel_direction.front_left = direction;
            if (current_command.mode == 0b00) {
                wheel_direction.rear_right = 0;
                wheel_direction.rear_left = 0;
            }
            break;
        case 0b10:
            wheel_direction.front_right = 45;
            wheel_direction.front_left = -45;
            wheel_direction.rear_right = 45;
            wheel_direction.rear_left = -45;
            break;
    }
    return 0;
}

float get_drive_speed() {
    return (float) current_command.speed / 127;
}
