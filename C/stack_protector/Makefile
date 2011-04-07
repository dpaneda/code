all: stack_protector

stack_protector:
	gcc -g3 -pedantic -Wstack-protector -fstack-protector -fstack-protector-all --param ssp-buffer-size=1 -o stack_protector stack_protector.c

clean:
	rm stack_protector
