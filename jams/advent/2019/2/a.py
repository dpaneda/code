#!/usr/bin/env python3

from enum import Enum

class Opcode(Enum):
    ADD = 1
    MUL = 2
    END = 99

def exec_instruction(program, ir):
    op = program[ir]
    operands = program[ir+1:ir+4]
    print(op, operands)

    if op == Opcode.END.value:
        return False
    else:
        a = program[operands[0]]
        b = program[operands[1]]
        if op == Opcode.ADD.value:
            c = a + b
        else:
            c = a * b
        program[operands[2]] = c
    return True

program = list(map(int, input().split(',')))
ir = 0
program[1] = 12
program[2] = 2

while exec_instruction(program, ir):
    ir += 4

print(program[0])
