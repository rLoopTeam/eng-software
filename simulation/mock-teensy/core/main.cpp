#include "WProgram.h"
#include <unistd.h>

extern void setup();
extern void loop();

extern "C" int main(void)
{

#ifdef USING_MAKEFILE

	// To use Teensy 3.0 without Arduino, simply put your code here.
	// For example:

#else

	// Arduino's main() function just calls setup() and loop()....
	setup();
	while (1) {
		loop();
		sleep(1);
		// yield();
	}

#endif

}
