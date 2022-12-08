#! /usr/bin/env python
import sys
from dataclasses import dataclass


grid = []
visible = set()

for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

n = len(grid)

def search(x, y, dx, dy):
    actual_height = -1
    while x < n and y < n and x >= 0 and y >= 0:
        if grid[y][x] > actual_height:
            visible.add((y, x))
            actual_height = grid[y][x]
        x += dx
        y += dy

def calculate_score(x, y):
    def peek(x, y, dx, dy):
        max_height = grid[y][x]
        distance = 0
        x += dx
        y += dy
        while x < n and y < n and x >= 0 and y >= 0:
            distance += 1
            if grid[y][x] >= max_height:
                return distance
            x += dx
            y += dy
        return distance

    score = 1
    score *= peek(x, y, 1, 0)
    score *= peek(x, y, -1, 0)
    score *= peek(x, y, 0, 1)
    score *= peek(x, y, 0, -1)
    return score

for i in range(0, n):
    search(0, i, 1, 0)
for i in range(0, n):
    search(i, 0, 0, 1)
for i in range(0, n):
    search(n - 1, i, -1, 0)
for i in range(0, n):
    search(i, n - 1, 0, -1)

print(len(visible))

best_score = 0
for x in range(0, n):
    for y in range(0, n):
        score = calculate_score(x, y)
        best_score = max(score, best_score)
print(best_score)
