#! /usr/bin/env python
import sys
from dataclasses import dataclass
from typing import Callable, Any
import time

@dataclass
class CPU:
    ticks: int = 1
    register: int = 1
    signal: int = 0

    def crt_draw(self):
        beam_position = (self.ticks - 1) % 40
        beam_lit = abs(self.register - beam_position) <= 1
        char = '#' if beam_lit else '.'
        print(char, end='', flush=True)
        if self.ticks % 40 == 0:
            print()
            time.sleep(0.2)
        time.sleep(0.02) 
 
    def add_tick(self):
        if (self.ticks - 20) % 40 == 0:
            # Time for signal strenght calculation
            self.signal += self.ticks * self.register
        self.crt_draw()
        self.ticks += 1

    def add_ticks(self, ticks):
        [self.add_tick() for _ in range(ticks)]

@dataclass
class Op:
    name: str
    cost: int
    code: Callable[Any, CPU]
    operand: int = 0

    def noop(self, cpu: CPU):
        pass

    def addx(self, cpu: CPU):
        cpu.register += self.operand
    
    def compile(s: str):
        match s.split():
            case ['noop']:
                return Op(name='noop', cost=1, code=Op.noop)
            case 'addx', value:
                return Op(name='addx', cost=2, operand=int(value), code=Op.addx)
            case _:
                raise Exception(f'Compile error on expression {s}')

    def exec(self, cpu):
        cpu.add_ticks(self.cost)
        self.code(self, cpu)

cpu = CPU()

for line in sys.stdin:
    op = Op.compile(line) 
    op.exec(cpu)
print(cpu)
