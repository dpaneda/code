#include <unistd.h>

void sleep_one(void) {
	sleep(1);
}

void sleep_five(void) {
	sleep(5);
}

void sleep_ten(void) {
	sleep(10);
}

int main (void) {
	while (1) {
		sleep_one();
		sleep_five();
		sleep_ten();
	}
}
