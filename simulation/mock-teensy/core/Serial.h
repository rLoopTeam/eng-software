#include <iostream>
using namespace std;

class Serial 
{
	public:
		void begin(int baud){
			cout << "Initialise serial comms..."<<endl;
		}
		void println(std::string str){
			cout << str << endl;
		}

} Serial;