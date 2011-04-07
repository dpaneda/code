	.file	"stack_use.c"
	.intel_syntax noprefix
	.text
.globl stack_1
	.type	stack_1, @function
stack_1:
	push	ebp
	mov	ebp, esp
	sub	esp, 16
	leave
	ret
	.size	stack_1, .-stack_1
.globl stack_2
	.type	stack_2, @function
stack_2:
	push	ebp
	mov	ebp, esp
	sub	esp, 16
	leave
	ret
	.size	stack_2, .-stack_2
.globl stack_4
	.type	stack_4, @function
stack_4:
	push	ebp
	mov	ebp, esp
	sub	esp, 16
	leave
	ret
	.size	stack_4, .-stack_4
.globl stack_100
	.type	stack_100, @function
stack_100:
	push	ebp
	mov	ebp, esp
	sub	esp, 112
	leave
	ret
	.size	stack_100, .-stack_100
.globl main
	.type	main, @function
main:
	push	ebp
	mov	ebp, esp
	call	stack_1
	call	stack_2
	call	stack_4
	call	stack_100
	mov	eax, 0
	pop	ebp
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.4.3-4ubuntu5) 4.4.3"
	.section	.note.GNU-stack,"",@progbits
