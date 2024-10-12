
// Potentiometer connection to A0 port
#define POT A0

int pot_val = 0;
int angle = 0;

void setup() {
  
  Serial.begin(9600);

  pinMode(POT, INPUT);

}

void loop() {

  //Map the voltage to the degree
  pot_val = analogRead(POT);
  angle = map(pot_val, 0, 1023, 0, 360);
  
  Serial.print("Voltage: ");
  Serial.println(pot_val);
  Serial.print("Angle: ");
  Serial.println(angle);

  delay(1000);
}
