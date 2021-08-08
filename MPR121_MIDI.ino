#include <Wire.h>
#include "Adafruit_MPR121.h"

Adafruit_MPR121 capacitive_touch_sensor = Adafruit_MPR121();

uint16_t last_touch_state = -1;

void setup() {
  // initialize PRNG with value of disconnected analog pin, to get a good random seed
  randomSeed(analogRead(0));

  Serial.begin(9600);

  while (!Serial) { // needed to keep leonardo/micro from starting too fast!
    delay(10);
  }
  
  //Serial.println("Adafruit MPR121 Capacitive Touch sensor test"); 
  
  // Default address is 0x5A, if tied to 3.3V its 0x5B
  // If tied to SDA its 0x5C and if SCL then 0x5D
  if (!capacitive_touch_sensor.begin(0x5A)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
  //Serial.println("MPR121 found!");
}

void loop() {
  // send out any touch information
  uint16_t touch_state = capacitive_touch_sensor.touched();
  if (touch_state != last_touch_state) {
    
    Serial.println(touch_state);
    
    last_touch_state = touch_state;
  }
}
