#include "motorController.h"

const int MESSAGE_LENGTH = 4;
byte receivedBytes[MESSAGE_LENGTH];   // an array to store the received data

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

void loop() {

  //check for new input
  recvWithEndMarker();

  // Variable definitions
  const float turn_motor_speed = 64;
  float speed_input = get_drive_speed();


  // ===========================================
  //
  // Motor forward/backward control
  //
  // ===========================================

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

  // ===========================================
  //
  // Motor left/right control
  //
  // ===========================================
  delay(1);
  //int pot_front_left_val = analogRead(POT_FRONT_LEFT);
  int pot_front_right_val = analogRead(POT_FRONT_RIGHT);
  //int actual_front_left_angle = map(pot_front_left_val, 0, 1023, -180, 180);
  int actual_front_right_angle = map(pot_front_right_val, 0, 1023, -180, 180);

  int desired_angle = current_command.direction;

  int front_right_angle_diff = normalize_angle(desired_angle - actual_front_right_angle);

  int angle_error_margin = 1;

  if (front_right_angle_diff > angle_error_margin) {
    digitalWrite(M_FRONT_LEFT_TURN_DIR, 1);
    digitalWrite(M_FRONT_RIGHT_TURN_DIR, 1);
    analogWrite(M_FRONT_LEFT_TURN, (int)(turn_motor_speed));
    analogWrite(M_FRONT_RIGHT_TURN, (int)(turn_motor_speed));
  } else if (front_right_angle_diff < angle_error_margin) {
    digitalWrite(M_FRONT_LEFT_TURN_DIR, 0);
    digitalWrite(M_FRONT_RIGHT_TURN_DIR, 0);
    analogWrite(M_FRONT_LEFT_TURN, (int)(turn_motor_speed));
    analogWrite(M_FRONT_RIGHT_TURN, (int)(turn_motor_speed));
  }
}

void recvWithEndMarker() {

  if (Serial.available() < MESSAGE_LENGTH) { return; }

  Serial.readBytes(receivedBytes, MESSAGE_LENGTH);
  processCommand(receivedBytes);

}

int normalize_angle(int angle) {
  // Ensure the angle is in the range [-180, 180]
  while (angle > 180) angle -= 360;
  while (angle < -180) angle += 360;
  return angle;
}