void stack_1() {
	char c;
}

void stack_2() {
	short c;
}

void stack_4() {
	int c;
}

void stack_100() {
	char c[100];
}

int main (void) {
	stack_1();
	stack_2();
	stack_4();
	stack_100();

	return 0;
}
