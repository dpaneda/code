#! /usr/bin/env python
import os
import sys
import time

grid = {}

def parse_point(p):
    return map(int, p.split(','))

for line in sys.stdin:
    path = line.split(' -> ')
    for i in range(len(path) - 1):
        x1, y1 = parse_point(path[i])
        x2, y2 = parse_point(path[i+1])
        if x1 > x2: 
            x1, x2 = x2, x1
        if y1 > y2: 
            y1, y2 = y2, y1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[(x,y)] = '#'

def drop_grain(grid, floor):
    def move(p):
        time.sleep(0.01)
        x, y = p
        moves = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        for move in moves:
            if move not in grid:
                del(grid[pos])
                grid[move] = 'o'
                return move
        return None


    ymax = max(p[1] for p in grid.keys())
    pos = 500, 0
    grid[pos] = 'o'
    while True:
        paint(grid)
        pos = move(pos)
        if not pos or pos[1] == floor:
            return True


def paint(grid):
    os.system('clear')
    xmin = min(p[0] for p in grid.keys())
    xmax = max(p[0] for p in grid.keys())
    ymin = 0
    ymax = max(p[1] for p in grid.keys())
    for y in range(ymin, ymax):
        for x in range(xmin, xmax):
            if (x, y) in grid:
                print(grid[(x, y)], end='')
            else:
                print('.', end='')
        print()

drops = 0
floor = 1 + max(p[1] for p in grid.keys())
while drop_grain(grid, floor):
    drops += 1
    if (500, 0) in grid:
        break
print(drops)
