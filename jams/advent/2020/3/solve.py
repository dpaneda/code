import sys
import math

grid = []

def grid_position(x, y):
    y %= len(grid)
    x %= len(grid[y])
    return grid[y][x]

def print_grid():
    for y in range(0, len(grid)):
        for x in range(0, 2 * len(grid[0])):
            print(grid_position(x, y), end='')
        print()

for line in sys.stdin:
    grid.append(line.strip())

print_grid()
multipliers = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 5 * [0]

for p in range(1, 1 + len(grid)):
    for i in range(0, 5):
        a, b = multipliers[i]
        x, y = p * a, p * b
        if y < len(grid) and grid_position(x, y) == '#':
            trees[i] += 1

print(trees[1])
print(math.prod(trees))
