#include "motorController.h"
#include <stdint.h>

 struct Command{
    uint8_t mode : 2;
    int8_t direction : 6;
    int8_t speed : 8;
};

struct Command current_command;
struct WheelDirection wheel_direction;

// Must be called to follow instructions of a new command
void processCommand(char* input1, char* input2){
    current_command.mode = *input1 >> 6;
    current_command.direction = *input1;
    current_command.speed = *input2;
}

void calculateWheelDirections(){
    int direction = current_command.direction;
    switch (current_command.mode){
            // Mode 1: Crab walk, all wheels activated
        case 0b01:
            wheel_direction.rear_right = direction;
            wheel_direction.rear_left = direction;
        default:
            wheel_direction.front_right = direction;
            wheel_direction.front_left = direction;
            // Mode 0: Normal, only front wheels activated
            if (current_command.mode == 0b00){
                wheel_direction.rear_right = 0;
                wheel_direction.rear_left = 0;
            }
            break;
            // Mode 2: 360, lock the wheels in a position that allows the robot to rotate
        case 0b10:
            wheel_direction.front_right = 45;
            wheel_direction.front_left = -45;
            wheel_direction.rear_right = 45;
            wheel_direction.rear_left = -45;
    }
}

float get_drive_speed(){
    return (float) current_command.speed / 127;
}




