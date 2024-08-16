const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;

// Define motor pins
#define M_LEFT_DRIVE 2
#define M_RIGHT_DRIVE 4
#define M_BACK_TURN 8
#define M_FRONT_TURN 10

// Define direction pins
#define D_LEFT_DRIVE 3
#define D_RIGHT_DRIVE 5
#define D_BACK_TURN 9
#define D_FRONT_TURN 11

void setup() {
  Serial.begin(9600);

  // Set digital pins with correct I/O direction
  for (int i=2; i<12; i++) {
    pinMode(i, OUTPUT);
  }
}

float speed_input = 0;
float turn_input = 0;
bool drive_dir = 0;
bool turn_dir = 0;

void loop() {
  recvWithEndMarker();
  if (newData == true) {
      speed_input = ((float)(int)(receivedChars[0]) - 53) / 10;
      turn_input = ((float)(int)(receivedChars[1]) - 53) / 10;
      if (speed_input < 0) {
        speed_input *= -1;
        drive_dir = 1;
      } else {
        drive_dir = 0;
      }
      if (turn_input < 0) {
        turn_input *= -1;
        turn_dir = 1;
      } else {
        turn_dir = 0;
      }
      newData = false;
  }
  digitalWrite(D_LEFT_DRIVE, drive_dir);
  digitalWrite(D_RIGHT_DRIVE, drive_dir);
  digitalWrite(D_BACK_TURN, turn_dir);
  digitalWrite(D_FRONT_TURN, turn_dir);

  analogWrite(M_LEFT_DRIVE, (int)(255 * speed_input));
  analogWrite(M_RIGHT_DRIVE, (int)(255 * speed_input));
  analogWrite(M_FRONT_TURN, (int)(255 * turn_input));
  analogWrite(M_BACK_TURN, (int)(255 * turn_input)); // make this 0 for only front turning

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

