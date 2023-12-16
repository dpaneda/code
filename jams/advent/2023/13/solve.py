#! /usr/bin/env python

import sys

def read_grid():
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        grid.append(line)
    return grid

def check_vertical_reflection(grid, n):
    errors = 0
    Y = len(grid)
    X = len(grid[0])
    check_size = min(n, X - n)
    for y in range(Y):
        for i in range(check_size):
            a, b = n - i - 1, n + i
            if grid[y][a] != grid[y][b]:
                errors += 1
    return errors

def check_horizontal_reflection(grid, n):
    errors = 0
    Y = len(grid)
    X = len(grid[0])
    check_size = min(n, Y - n)
    for x in range(X):
        for i in range(check_size):
            a, b = n - i - 1, n + i
            if grid[a][x] != grid[b][x]:
                errors += 1
    return errors

def check_grid(grid, errors):
    Y = len(grid)
    X = len(grid[0])
    for i in range(1, Y):
        if check_horizontal_reflection(grid, i) == errors:
            return 100 * i
    for i in range(1, X):
        if check_vertical_reflection(grid, i) == errors:
            return i
 
n1 = n2 = 0
while True:
    grid = read_grid()
    if not grid:
        break
    n1 += check_grid(grid, 0)
    n2 += check_grid(grid, 1)
print(n1, n2)
