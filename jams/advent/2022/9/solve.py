#! /usr/bin/env python

import sys

head_positions = []
tail_positions = set()

head = [0, 0]
tail = [0, 0]

move_to = { 'U': (0, +1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

def move_tail():
    if head[0] - tail[0] == 2:
        tail[0] = head[0] - 1
        tail[1] = head[1]
    if head[1] - tail[1] == 2:
        tail[1] = head[1] - 1
        tail[0] = head[0]
    if head[0] - tail[0] == -2:
        tail[0] = head[0] + 1
        tail[1] = head[1]
    if head[1] - tail[1] == -2:
        tail[1] = head[1] + 1
        tail[0] = head[0] 
    tail_positions.add(tuple(tail))

for line in sys.stdin:
    where, count = line.split()
    for _ in range(0, int(count)):
        head[0] += move_to[where][0]
        head[1] += move_to[where][1]
        move_tail()

print(tail_positions)
print(len(tail_positions))
