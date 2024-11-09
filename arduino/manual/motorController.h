#ifndef MOTOR_CONTROLLER_H
#define MOTOR_CONTROLLER_H

struct WheelDirection;
void processCommand(char *);
int calculateWheelDirections();
float get_drive_speed(char *);

#endif