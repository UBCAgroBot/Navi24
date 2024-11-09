#ifndef MOTOR_CONTROLLER_H
#define MOTOR_CONTROLLER_H

#include <stdint.h>

// Define constants
#define M_REAR_LEFT_DRIVE 2
#define M_FRONT_LEFT_DRIVE 3
#define M_REAR_RIGHT_DRIVE 4
#define M_FRONT_RIGHT_DRIVE 5
#define MAX_SPEED 255

// Structures for commands and wheel directions
struct Command {
    int8_t mode;
    int8_t direction;
    int8_t speed;
};

struct WheelDirection {
    int16_t front_right;
    int16_t front_left;
    int16_t rear_right;
    int16_t rear_left;
};

// Declare global variables as extern to avoid multiple definitions
extern WheelDirection wheel_direction;
extern Command current_command;
extern const int MAX_ROTATION_ANGLE;

// Function declarations
int clamp(int val, int min_val, int max_val);
void processCommand(char* receivedChars);
int calculateWheelDirections();
float get_drive_speed();

#endif
