#! /usr/bin/env python

import sys

draw_numbers = map(int, input().split(','))

grids = []

def read_grid(grids):
    grid = []
    for a in range(5):
        l = list(map(int, input().split()))
        grid.append(l)
    grids.append(grid)

def mark_number(grids, n):
    for grid in grids:
        for row in grid:
            if row.count(n):
                i = row.index(n)
                row[i] = 0

def check_row(grid, n):
    return sum(grid[n]) == 0

def check_column(grid, n):
    s = 0
    for row in grid:
        s += row[n]
    return s == 0

def score(grid):
    n = 0
    for row in grid:
        n += sum(row)
    return n

def check_grids(grids):
    sc = 0
    for grid in grids:
        for i in range(5):
            if check_row(grid, i) or check_column(grid, i):
                grids.remove(grid)
                sc = score(grid)
                break
    return sc

for _ in sys.stdin:
    read_grid(grids)

for grid in grids:
    print(grid)
print(draw_numbers)

for n in draw_numbers:
    if not grids:
        break
    else:
        print(len(grids))
    mark_number(grids, n)
    sc = check_grids(grids)
    if sc:
        print(n * sc)
