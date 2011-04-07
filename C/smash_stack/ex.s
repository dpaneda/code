	.file	"ex.c"
	.intel_syntax noprefix
	.text
.globl function
	.type	function, @function
function:
	push	ebp
	mov	ebp, esp
	sub	esp, 16
	mov	DWORD PTR [ebp-5], 1094795585
	mov	BYTE PTR [ebp-1], 0
	mov	DWORD PTR [ebp-15], 1111638594
	mov	DWORD PTR [ebp-11], 1111638594
	mov	WORD PTR [ebp-7], 66
	leave
	ret
	.size	function, .-function
.globl main
	.type	main, @function
main:
	lea	ecx, [esp+4]
	and	esp, -16
	push	DWORD PTR [ecx-4]
	push	ebp
	mov	ebp, esp
	push	ecx
	sub	esp, 12
	mov	DWORD PTR [esp+8], 3
	mov	DWORD PTR [esp+4], 2
	mov	DWORD PTR [esp], 1
	call	function
	add	esp, 12
	pop	ecx
	pop	ebp
	lea	esp, [ecx-4]
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.3.2-1ubuntu11) 4.3.2"
	.section	.note.GNU-stack,"",@progbits
