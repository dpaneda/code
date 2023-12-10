#! /usr/bin/env python

import sys
from collections import defaultdict

# Delta of the exits as (dx, dy)
exits = {
    '|':((0, -1), (0, 1)),
    '-':((-1, 0), (1, 0)),
    'L':((0, -1), (1, 0)),
    'J':((0, -1), (-1, 0)),
    '7':((0, 1), (-1, 0)),
    'F':((0, 1), (1, 0)),
}

# The grid is a dictionary of sets which contains the exits
grid = defaultdict(set)

# The axis grow to the right and down (non-standard but convenient)
lines = sys.stdin.readlines()

start = None
for y in range(len(lines)):
    for x in range(len(lines[y])):
        c = lines[y][x]
        if c == 'S':
            start = (x, y)
        for (dx, dy) in exits.get(c, []):
            a = (x, y)
            b = (x + dx, y + dy)
            grid[a].add(b)
            if b == start:
                grid[b].add(a)

visited = set()
border = set([start])
while border:
    new_border = set()
    for p in border:
        for p2 in grid[p]:
            if p2 not in visited:
                new_border.add(p2)
    visited |= border
    border = new_border

print(len(visited) // 2)
