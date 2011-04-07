#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void f1 (char *p) {
	strcpy (p, "1111111111111");
}


int main (void) {
	char p[37];
//	char *p = malloc(37);

	f1(p);
	printf("%s\n", p);
	printf("%c\n", p[0]);
	printf("%c\n", p[1]);

	return 0;
}
