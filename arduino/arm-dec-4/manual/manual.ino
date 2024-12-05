#include "motorController.h"

const byte MESSAGE_LENGTH = 4;
char receivedChars[MESSAGE_LENGTH];   // an array to store the received data

// Potentiometer connections to analog ports
#define POT_FRONT_RIGHT A0
#define POT_FRONT_LEFT A1

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

  pinMode(POT_FRONT_RIGHT, INPUT);
  pinMode(POT_FRONT_LEFT, INPUT);

}

float speed_input = 0;
float turn_input = 64;
bool drive_dir = 0;
bool turn_dir = 0;

void loop() {

  //check for new input
  recvWithEndMarker();
  speed_input = get_drive_speed();

  //go backwards
  if(speed_input < 0){
    digitalWrite(M_REAR_LEFT_DRIVE_DIR, 0);
    digitalWrite(M_REAR_RIGHT_DRIVE_DIR, 1);
    digitalWrite(M_FRONT_LEFT_DRIVE_DIR, 0);
    digitalWrite(M_FRONT_RIGHT_DRIVE_DIR, 1);  
  }
  //go forwards
  else if(speed_input > 0){
    digitalWrite(M_REAR_LEFT_DRIVE_DIR, 1);
    digitalWrite(M_REAR_RIGHT_DRIVE_DIR, 0);
    digitalWrite(M_FRONT_LEFT_DRIVE_DIR, 1);
    digitalWrite(M_FRONT_RIGHT_DRIVE_DIR, 0);  
    
  }

  analogWrite(M_REAR_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_FRONT_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_REAR_RIGHT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_FRONT_RIGHT_DRIVE, (int)(MAX_SPEED * speed_input));
}

void recvWithEndMarker() {

  if (Serial.available() < MESSAGE_LENGTH) { return; }

  Serial.readBytes(receivedChars, MESSAGE_LENGTH);
  processCommand(receivedChars);

}
