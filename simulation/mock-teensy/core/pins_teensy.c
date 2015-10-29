
#include "core_pins.h"

// this is not present in the original file!
#include <Print.h>

void pinMode(uint8_t pin, uint8_t mode)
{

  if(mode == OUTPUT){
    printf("PIN %d is set to OUTPUT\n", pin);
  }
  else{
    printf("PIN %d is set to INPUT \n", pin);
  }

}

void digitalWrite(uint8_t pin, uint8_t val)
{

  // printf("digital write\n");
  if(val == HIGH){
    printf("PIN %d ON\n", pin);
  }
  else{
    printf("PIN %d OFF\n", pin);
  }

}
