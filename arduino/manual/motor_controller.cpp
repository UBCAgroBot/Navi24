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

void processCommand(char * receivedChars) {
  // One char should equal one int8_t
  current_command = {receivedChars[0], receivedChars[1], receivedChars[2]};

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
    int direction = current_command.direction;
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
