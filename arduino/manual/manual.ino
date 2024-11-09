#include "motorController.h"
#include <Arduino.h>

const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;

// Define motor pins
#define M_REAR_LEFT_DRIVE 2
#define M_FRONT_LEFT_DRIVE 3
#define M_REAR_RIGHT_DRIVE 4
#define M_FRONT_RIGHT_DRIVE 5


// Define direction pins
#define M_REAR_LEFT_DRIVE_DIR 30
#define M_FRONT_LEFT_DRIVE_DIR 31
#define M_REAR_RIGHT_DRIVE_DIR 32
#define M_FRONT_RIGHT_DRIVE_DIR 33

#define MAX_SPEED 255


void setup() {
  Serial.begin(9600);

  // Set digital pins with correct I/O direction
  for (int i=2; i<6; i++) {
    pinMode(i, OUTPUT);
    pinMode(28+i, OUTPUT);
  }

}

float speed_input = 0;
float turn_input = 0;
bool drive_dir = 0;
bool turn_dir = 0;

void loop() {
  recvWithEndMarker();
  byte data[] = {255, 255};
  Serial.write(data, 2);
  if (newData == true) {
    processCommand(&receivedChars[0], &receivedChars[1]);
    speed_input = get_drive_speed();
    newData = false;
  }

  analogWrite(M_REAR_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_FRONT_LEFT_DRIVE, (int)(MAX_SPEED * speed_input));
  analogWrite(M_REAR_RIGHT_DRIVE, (int)(MAX_SPEED * turn_input));
  analogWrite(M_FRONT_RIGHT_DRIVE, (int)(MAX_SPEED * turn_input)); 

  Serial.print(speed_input);
  Serial.print(" ");
  Serial.print(turn_input);
  Serial.print(" Drive Dir: ");
  Serial.print(drive_dir);
  Serial.print(" Turn Dir: ");
  Serial.println(turn_dir);

}

void recvWithEndMarker() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (rc != endMarker) {
            receivedChars[ndx] = rc;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
            newData = true;
        }
    }
}

