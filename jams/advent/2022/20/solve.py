#! /usr/bin/env python
import sys

to_move = [int(l) for l in sys.stdin.readlines()]
to_move = list(zip(range(len(to_move)), to_move))
file = list(to_move)

def move(l, what):
    rotation = what[1]
    n = len(l) - 1
    rotation = rotation % n
    orig_index = l.index(what)
    dest_index = (orig_index + rotation) % n
    l.remove(what)
    l2 = l[:dest_index]
    l2.append(what)
    l2 += l[dest_index:]
    return l2

def get_coordinates(l):
    for i in range(len(l)):
        if l[i][1] == 0:
            break
    return l[(i + 1000) % len(l)][1] + l[(i + 2000) % len(l)][1] +  l[(i + 3000) % len(l)][1]

for what in to_move:
    file = move(file, what)

print(f"Solution for part 1 is {get_coordinates(file)}")

# Part 2
to_move = [(a, b * 811589153) for a, b in to_move]
file = list(to_move)

for _ in range(10):
    for what in to_move:
        file = move(file, what)

print(f"Solution for part 2 is {get_coordinates(file)}")
