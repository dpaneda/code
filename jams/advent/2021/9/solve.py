#! /usr/bin/env python
import sys
import math

grid = []

for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

print(grid)

risk = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        p = grid[y][x]
        if x > 0 and grid[y][x - 1] <= p:
            continue
        if y > 0 and grid[y - 1][x] <= p:
            continue
        if y < len(grid) - 1 and grid[y + 1][x] <= p:
            continue
        if x < len(grid[0]) - 1 and grid[y][x + 1] <= p:
            continue
        risk += p + 1

print(risk)

def expand_basin(grid, x, y):
    basin = set()
    explore = set()
    explore.add((x, y))

    while explore:
        x, y = explore.pop()
        if x > 0 and grid[y][x - 1] != 9:
            explore.add((x - 1, y))
        if y > 0 and grid[y - 1][x] != 9:
            explore.add((x, y - 1))
        if y < len(grid) - 1 and grid[y + 1][x] != 9:
            explore.add((x, y + 1))
        if x < len(grid[0]) - 1 and grid[y][x + 1] != 9:
            explore.add((x + 1, y))
        basin.add((x, y))
        explore -= basin
    return basin

explored = set()
basins = []
basin_sizes = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (x, y) in explored or grid[y][x] == 9:
            continue
        basin = expand_basin(grid, x, y)
        explored |= basin
        basins.append(basin)
        basin_sizes.append(len(basin))

basin_sizes.sort()
print(math.prod(basin_sizes[-3:]))
