#include <Wire.h>
#include <Wiichuck.h>

#define enA 10
#define in1 9
#define in2 8

Wiichuck wii;

int rotDirection = 0;
int pressed = 0;

void setup() {  
  Serial.begin(9600);
  wii.init();  
  wii.calibrate();  // calibration
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // Set initial rotation direction
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void loop() {
  if (wii.poll()) {
    int potValue = wii.joyY(); // Read potentiometer value
    int pwmOutput = map(potValue, 0, 1023, 0, 255); // Map the potentiometer value from 0 to 255
    analogWrite(enA, pwmOutput); // Send PWM signal to L298N Enable pin
    
    Serial.print(potValue);
    Serial.print("  \t");
    Serial.println(pressed);
    
    if (wii.buttonZ() == 1) {
      pressed = !pressed;
    }
    if (pressed == 1 & rotDirection == 0) {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      rotDirection = 1;
      delay(20);
    }
    if (pressed == 0 & rotDirection == 1) {
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      rotDirection = 0;
      delay(20);
    }
  }
} 
