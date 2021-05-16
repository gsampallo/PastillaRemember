#include "Arduino.h"
#include "Musica.h"


Musica::Musica(int pin) {
  tonePin = pin;

}

  

void Musica::reproducir() {
  
    tone(tonePin, 659, 71.4285);
    delay(79.365);
    delay(39.6825);
    tone(tonePin, 659, 71.4285);
    delay(79.365);
    delay(158.73);
    tone(tonePin, 659, 71.4285);
    delay(79.365);
    delay(158.73);
    tone(tonePin, 523, 71.4285);
    delay(79.365);
    delay(39.6825);
    tone(tonePin, 659, 71.4285);
    delay(79.365);
    delay(158.73);
}

void Musica::tono() {
  tone(tonePin, 659, 71.4285);
  delay(79.365);
  tone(tonePin, 659, 71.4285);
  delay(39.6825);
}
