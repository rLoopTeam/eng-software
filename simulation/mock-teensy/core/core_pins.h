
#ifndef _core_pins_h_
#define _core_pins_h_


#define HIGH		1
#define LOW		0

#define INPUT		0
#define OUTPUT		1

void pinMode(uint8_t pin, uint8_t mode);
void digitalWrite(uint8_t pin, uint8_t val);

#endif
