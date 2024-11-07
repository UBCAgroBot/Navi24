#include 'motorController.h'
#include <cstdint>
#include <algorithm>

 struct Command{
    int8_t mode : 2;
    int8_t direction : 6;
    int8_t speed : 8;
};

struct WheelDirection{
    int16_t front_right;
    int16_t front_left;
    int16_t rear_right;
    int16_t rear_left;
};

MAX_ROTATION_ANGLE = 90;

WheelDirection wheel_direction = {0, 0, 0, 0};
Command current_command = {0, 0,0 };

// Must be called to follow instructions of a new command
void processCommand(char* input1, char* input2){
    current_command.mode = std::clamp(-MAX_ROTATION_ANGLE, (int) (*input1 >> 6) * 3, MAX_ROTATION_ANGLE);
    current_command.direction = *input1;
    current_command.speed = *input2;
}

int calculateWheelDirections(){
    direction = current_command.direction;
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




