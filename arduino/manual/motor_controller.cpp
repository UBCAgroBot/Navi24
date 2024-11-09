#include "motorController.h"

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

void processCommand(char* input1, char* input2) {
    current_command.mode = clamp((*input1 >> 6) * 3, -MAX_ROTATION_ANGLE, MAX_ROTATION_ANGLE);
    current_command.direction = *input1;
    current_command.speed = *input2;
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
