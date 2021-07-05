/*
 * TIPE 2022
 * Auteur: Armand Wayoff
 * Date: 05/07/2021
 */


#include <Wire.h>
#include <Wiichuck.h>

// Pins L298N
#define enA 10
#define in1 9
#define in2 8

Wiichuck wii;

int rotDirection = 0;
int current;
int previous = 0;

void setup() {  
  Serial.begin(9600);
  
  wii.init();  
  wii.calibrate(); 
  
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // Sens de rotation initial
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void loop() {
  if (wii.poll()) {
    int potValue = wii.joyY(); // Lecture de la valeur du joystick selon l'axe Y
    int pwmOutput = map(potValue, 0, 1023, 0, 255); 
    analogWrite(enA, pwmOutput); 

    current = wii.buttonZ();
    if (current == 1 && previous == 0) {
      if (rotDirection == 0) {
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        rotDirection = 1;
        delay(20);
      } else {
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        rotDirection = 0;
        delay(20);
      }
    } 
    previous = current;
  }
} 
