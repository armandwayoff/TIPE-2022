#include <Stepper.h>

const int STEPS_PER_REV = 200;

Stepper stepper1(STEPS_PER_REV, 3, 4, 5, 6);
Stepper stepper2(STEPS_PER_REV, 8, 9, 10, 11);


void setup() {
  Serial.begin(9600);
  stepper1.setSpeed(360);
  stepper2.setSpeed(360);
}

void loop() {
  if (Serial.available() == 1) {
    userInput = Serial.read();
    stepper_NEMA17.step(userInput/100);
  }
}
