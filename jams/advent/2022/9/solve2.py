#! /usr/bin/env python

import sys

tail_positions = set()

rope = []
for _ in range(0, 10):
    rope.append([0, 0])

move_to = { 'U': (0, +1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

def move_tail(head, tail):
    if head[0] - tail[0] == 2 and head[1] - tail[1] == 2:
        tail[0] = head[0] - 1
        tail[1] = head[1] - 1
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == -2:
        tail[0] = head[0] - 1
        tail[1] = head[1] + 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == -2:
        tail[0] = head[0] + 1
        tail[1] = head[1] + 1
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == 2:
        tail[0] = head[0] + 1
        tail[1] = head[1] - 1
    elif head[0] - tail[0] == 2:
        tail[0] = head[0] - 1
        tail[1] = head[1]
    elif head[1] - tail[1] == 2:
        tail[1] = head[1] - 1
        tail[0] = head[0]
    elif head[0] - tail[0] == -2:
        tail[0] = head[0] + 1
        tail[1] = head[1]
    elif head[1] - tail[1] == -2:
        tail[1] = head[1] + 1
        tail[0] = head[0] 


for line in sys.stdin:
    where, count = line.split()
    for _ in range(0, int(count)):
        rope[0][0] += move_to[where][0]
        rope[0][1] += move_to[where][1]
        for i in range(0, 9):
            move_tail(rope[i], rope[i+1])
        tail_positions.add(tuple(rope[9]))

print(tail_positions)
print(len(tail_positions))
