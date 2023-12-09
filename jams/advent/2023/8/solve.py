#! /usr/bin/env python

import sys
import re
from math import lcm

path = input()
pos = []
g = {}
for line in sys.stdin:
    r = re.search(r"(\w+) = \((\w+), (\w+)\)", line.strip())
    if r:
        origin, left, right = r.groups()
        g[origin] = (left, right)
        if origin[-1] == 'A':
            pos.append(origin)

def get_steps(pos):
    steps = 0
    while pos[-1] != "Z":
        d = path[steps % len(path)]
        index = 0 if d == 'L' else 1
        pos = g[pos][index]
        steps += 1
    return steps


# This works because how the input is crafted (because
# the first node ending in Z can be different than ZZZ
print(f"Part 1 solution is {get_steps('AAA')}")
steps = list(map(get_steps, pos))
print(f"Part 2 solution is {lcm(*steps)}")
