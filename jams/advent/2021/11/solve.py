#! /usr/bin/env python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x : int
    y : int

def adjacent(p : Point):
    l = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            l.append(Point(p.x + dx, p.y + dy))
    return l

def step(grid):
    # Energy level increase
    for p in grid:
        grid[p] += 1

    flashed = set()
    # Resolve flashes
    nflashed = -1
    while nflashed != len(flashed):
        nflashed = len(flashed)
        for p, v in grid.items():
            if v < 10 or p in flashed:
                continue
            for p2 in adjacent(p):
                if p2 in grid:
                    grid[p2] += 1
                flashed.add(p)
    for p in flashed:
        grid[p] = 0
    return nflashed

grid = {}

for x in range(0, 10):
    line = input()
    for y in range(0, 10):
        grid[Point(x, y)] = int(line[y])

total_flash = 0
for i in range(1, 100000):
    flashed = step(grid)
    if flashed == 100:
        print(i)
        break
    total_flash += flashed
print(total_flash)
