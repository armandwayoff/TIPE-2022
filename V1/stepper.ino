#include <Stepper.h>

const int STEPS_PER_REV = 200;

Stepper stepper_NEMA17(STEPS_PER_REV, 8, 9, 10, 11);

void setup() {
    stepper_NEMA17.setSpeed(360 ();
}

void loop() {
  stepper_NEMA17.step(STEPS_PER_REV/100);
}
