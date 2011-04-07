section .text
global _start

msg db 'Hello, world!',0Ah
len equ $ - msg
_start:
	mov edx, len
	mov ecx,msg
	mov ebx,1
	mov eax,4
	int 80h
	mov eax,1
	int 80h
