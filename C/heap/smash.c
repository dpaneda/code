#include <stdlib.h>
#include <stdio.h>
#include <mcheck.h>

char * malloc_da(int size) {
	char *a;
	int i;

	a = malloc(size);

	for(i=0; i<size; i++)
		a[i] = 0xda;

	return a;
}

int main (void) {
	char *a;
	int b;
	int i;

	//mtrace();

	mcheck_pedantic(0);

	for (i=0; i<10; i++) {
		a = malloc_da(12);
		printf("Obtained ptr in %p\n", a);
	}

	for (i=0; i<10; i++) {
		a = malloc_da(12);
		printf("Obtained ptr in %p\n", a);
		free(a);
		printf("Freed %p\n", a);
	}

	for (i=0; i<10; i++) {
		a = malloc_da(12);
		printf("Obtained ptr in %p\n", a);
	}

/*	
	b = malloc_usable_size(a);

	printf("I ask for 12 but i can use %d\n", b);
*/	

	//muntrace();

	sleep(50);

	return 0;
}
