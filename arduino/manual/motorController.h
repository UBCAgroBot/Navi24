#ifndef MOTOR_CONTROLLER_H
#define MOTOR_CONTROLLER_H
#include <stdint.h>

struct WheelDirection{
    int16_t front_right;
    int16_t front_left;
    int16_t rear_right;
    int16_t rear_left;
};

extern struct WheelDirection wheel_direction;
void processCommand(char *, char*);
void calculateWheelDirections();
float get_drive_speed();

#endif