#! /usr/bin/env python
import sys
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Point:
    x : int
    y : int
    steps : int = field(compare=False, hash=False)

def read_wire():
    wire = set()
    moves = input().split(',')
    x, y, steps = 0, 0, 0
    for move in moves:
        direction, n = move[0], int(move[1:])
        for i in range(n):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            steps += 1
            wire.add(Point(x, y, steps))
    return wire

wire1 = read_wire()
wire2 = read_wire()

closest = 999999
for point in wire1 & wire2:
    print(point)
    n = abs(point.x) + abs(point.y)
    if n < closest:
        closest = n
print(closest)

closest = 99999999
for p1 in wire1:
    for p2 in wire2:
        if p1 != p2: 
            continue
        print(p1)
        n = p1.steps + p2.steps
        if n < closest:
            closest = n
print(closest)
