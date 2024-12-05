#ifndef MOTOR_CONTROLLER_H
#define MOTOR_CONTROLLER_H

#include <stdint.h>
#include <Arduino.h>

// Define constants
#define M_REAR_LEFT_DRIVE 2
#define M_FRONT_LEFT_DRIVE 3
#define M_REAR_RIGHT_DRIVE 4
#define M_FRONT_RIGHT_DRIVE 5
#define M_REAR_LEFT_TURN 6
#define M_FRONT_LEFT_TURN 7
#define M_REAR_RIGHT_TURN 8
#define M_FRONT_RIGHT_TURN 9
#define MAX_SPEED 255

// Structures for commands and wheel directions
struct Command {
    int8_t mode;
    int16_t direction;
    int8_t speed;
};


// Declare global variables as extern to avoid multiple definitions
extern Command current_command;

// Function declarations
void processCommand(byte * receivedBytes);
float get_drive_speed();

#endif
