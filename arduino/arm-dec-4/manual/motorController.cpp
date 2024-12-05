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

void processCommand(byte * receivedBytes) {
  // One char should equal one int8_t
  current_command.mode = receivedBytes[0];
  uint8_t lowByte = static_cast<uint8_t>(receivedBytes[1]); // Least significant byte
  uint8_t highByte = static_cast<uint8_t>(receivedBytes[2]); // Most significant byte
  current_command.direction = static_cast<int16_t>(lowByte | (highByte << 8));
  current_command.speed = receivedBytes[3];

  Serial.print("mod: ");
  Serial.print(current_command.mode);
  Serial.print(", dir: ");
  Serial.print(current_command.direction);
  Serial.print(", spd: ");
  Serial.print(current_command.speed);
  Serial.println();

  wheel_direction.front_right = current_command.direction;
  wheel_direction.front_left = current_command.direction;
  wheel_direction.rear_right = 0;
  wheel_direction.rear_left = 0;

}

float get_drive_speed() {
    return (float) current_command.speed / 127;
}
