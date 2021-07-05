/*
 * TIPE 2022
 * Auteur: Armand Wayoff
 * Date: 05/07/2021
 */


#include <Wire.h>
#include <Wiichuck.h>

#define enA 10
#define in1 9
#define in2 8

Wiichuck wii;

int sens_rot = 0;
int etat_actuel;
int etat_precedent = 0;
int dt = 20;

void setup() 
{  
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

void loop() 
{
  if (wii.poll()) 
  {
    int valeur_joystick = wii.joyY(); 
    int sortie_pwm = map(valeur_joystick, 0, 1023, 0, 255); 
    analogWrite(enA, sortie_pwm);
    
    etat_actuel = wii.buttonZ();
    if (etat_actuel == 1 && etat_precedent == 0) 
    {
      if (sens_rot == 0) 
      {
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        sens_rot = 1;
        delay(dt);
      } 
      else 
      {
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        sens_rot = 0;
        delay(dt);
      }
    } 
    etat_precedent = etat_actuel;
  }
} 
