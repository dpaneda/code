#! /usr/bin/env python

import sys

def read_grid():
    grid = []
    rocks = set()
    y = 0
    for line in sys.stdin:
        line = line.strip()
        grid.append(line)
        for x, c in enumerate(line):
            if c == 'O':
                rocks.add((x, y))
        y += 1
    return grid, rocks

def go_north(grid, rocks):
    X = len(grid[0])
    Y = len(grid)
    for x in range(X):
        floor = 0
        for y in range(Y):
            if grid[y][x] == '#':
                floor = y + 1
            elif (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add((x, floor))
                floor += 1
    return rocks

def go_south(grid, rocks):
    X = len(grid[0])
    Y = len(grid)
    for x in range(X):
        floor = Y - 1
        for y in range(Y - 1, -1, -1):
            if grid[y][x] == '#':
                floor = y - 1
            elif (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add((x, floor))
                floor -= 1
    return rocks
 
def go_west(grid, rocks):
    X = len(grid[0])
    Y = len(grid)
    for y in range(Y):
        floor = 0
        for x in range(X):
            if grid[y][x] == '#':
                floor = x + 1
            elif (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add((floor, y))
                floor += 1
    return rocks

def go_east(grid, rocks):
    X = len(grid[0])
    Y = len(grid)
    for y in range(Y):
        floor = X - 1
        for x in range(X - 1, -1, -1):
            if grid[y][x] == '#':
                floor = x - 1
            elif (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add((floor, y))
                floor -= 1
    return rocks

def cycle(rocks):
    global grid
    rocks = set(rocks)
    go_north(grid, rocks)
    go_west(grid, rocks)
    go_south(grid, rocks)
    go_east(grid, rocks)
    return frozenset(rocks)

def north_weight(rocks, N):
    return sum([N - r[1] for r in rocks])

positions = {}
grid, rocks = read_grid()
N = len(grid)
go_north(grid, rocks)
print(f"Part 1: {north_weight(rocks, N)}")
go_west(grid, rocks)
go_south(grid, rocks)
go_east(grid, rocks)
i = 1
loop_size = 0
CYCLES = 1000000000
while i < CYCLES:
    rocks = cycle(rocks)
    i += 1
    if not loop_size and rocks in positions:
        loop_size = i - positions[rocks]
        loops = (CYCLES - i) // loop_size
        i += loop_size * loops
    else:
        positions[rocks] = i

print(f"Part 2: {north_weight(rocks, N)}")
