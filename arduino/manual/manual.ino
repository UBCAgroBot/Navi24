#include "motorController.h"

const byte MESSAGE_LENGTH = 16;
char receivedChars[MESSAGE_LENGTH];   // an array to store the received data

boolean newData = false;

// Define motor pins
#define M_REAR_LEFT_DRIVE 2
#define M_FRONT_LEFT_DRIVE 3
#define M_REAR_RIGHT_DRIVE 4
#define M_FRONT_RIGHT_DRIVE 5
#define M_REAR_LEFT_TURN 6
#define M_FRONT_LEFT_TURN 7
#define M_REAR_RIGHT_TURN 8
#define M_FRONT_RIGHT_TURN 9

// Define direction pins
#define M_REAR_LEFT_DRIVE_DIR 30
#define M_FRONT_LEFT_DRIVE_DIR 31
#define M_REAR_RIGHT_DRIVE_DIR 32
#define M_FRONT_RIGHT_DRIVE_DIR 33
#define M_REAR_LEFT_TURN_DIR 34
#define M_FRONT_LEFT_TURN_DIR 35
#define M_REAR_RIGHT_TURN_DIR 36
#define M_FRONT_RIGHT_TURN_DIR 37

void setup() {
  Serial.begin(9600);

  // Set digital pins with correct I/O direction
  for (int i = 2; i < 10; i++) {
    pinMode(i, OUTPUT);
    pinMode(28 + i, OUTPUT);
  }
}

float speed_input = 0;
float turn_input = 64;
bool drive_dir = 0;
bool turn_dir = 0;

void loop() {

  recvWithEndMarker();
  
  
  if (newData == true) {
    processCommand(receivedChars);  // corrected function name
    speed_input = get_drive_speed();
    newData = false;
  }

  analogWrite(M_REAR_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_FRONT_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_REAR_RIGHT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_FRONT_RIGHT_DRIVE, (int)(MAX_SPEED * speed_input));

  if(wheel_direction.front_right != 0){
    analogWrite(M_REAR_LEFT_TURN, (int)(turn_input));
    analogWrite(M_FRONT_LEFT_TURN, (int)(turn_input));
    analogWrite(M_REAR_RIGHT_TURN, (int)(turn_input));
    analogWrite(M_FRONT_RIGHT_TURN, (int)(turn_input));
    
  }  

}

void recvWithEndMarker() {
  if (Serial.available() == 0) { return; }

  String received = Serial.readString();

  // If string is wrong size, abort
  if (received.length() < MESSAGE_LENGTH) {
    Serial.print("INVALID MESSAGE LENGTH");
    return;
  }

  for (byte i = 0; i < MESSAGE_LENGTH; i++) {
    receivedChars[i] = received[i];
  }

  newData = true;
}
