#! /usr/bin/env python
import sys, math

grid = []

for line in sys.stdin:
    if line.find('S') != -1:
        start = len(grid), line.find('S')
    if line.find('E') != -1:
        end = len(grid), line.find('E')
    line = line.replace('S', 'a').replace('E', 'z')
    grid.append(line)

N = len(grid)
M = len(grid[0])

def height(p):
    y, x = p
    return ord(grid[y][x]) - ord('a')

def neighbors(p):
    n = set()
    y, x = p
    if y > 0:
        n.add((y - 1, x))
    if x > 0:
        n.add((y, x - 1))
    if y < N - 1:
        n.add((y + 1, x))
    if x < M - 1:
        n.add((y, x + 1))
    return n

def expand_frontier(frontier, best_paths):
    new_frontier = set()
    for p in frontier:
        for p2 in neighbors(p):
            if p2 not in best_paths and height(p2) <= height(p) + 1:
                new_frontier.add(p2)
                best_paths[p2] = best_paths[p] + 1
    return new_frontier

def find_best_path(p):
    frontier = set([p])
    best_paths = {p: 0}

    while frontier:
        frontier = expand_frontier(frontier, best_paths)
        if end in best_paths:
            return best_paths[end]
    return math.inf

best_cost = math.inf
for y in range(N):
    for x in range(M):
        if grid[y][x] == 'a':
            best_cost = min(best_cost, find_best_path((y, x)))

print(find_best_path(start))
print(best_cost)
