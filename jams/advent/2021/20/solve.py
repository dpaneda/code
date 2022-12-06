#! /usr/bin/env python
import sys
from dataclasses import dataclass

enhance_array = input()

input()

@dataclass(frozen=True)
class Point():
    x : int
    y : int

    def adjacent(self):
        l = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                l.append(Point(self.x + dx, self.y + dy))
        return l

input_grid = {}

y = 0

for line in sys.stdin:
    line = line.strip()
    N = len(line)
    for x in range(0, len(line)):
        p = Point(x, y)
        input_grid[p] = 1 if line[x] == '#' else 0
    y += 1

def enhance(grid, e, offset):
    out_grid = {}
    for y in range(-offset, N + offset):
        for x in range(-offset, N + offset):
            p = Point(x, y)
            l = p.adjacent()
            n = 0
            for p2 in l:
                v = grid.get(p2, 0)
                n = (n * 2) + v
            out_grid[Point(x, y)] = 1 if e[n] == '#' else 0
    return out_grid

def print_grid(g, offset):
    for y in range(-offset, N + offset):
        for x in range(-offset, N + offset):
            if g[Point(x, y)]:
                print('#', end='')
            else:
                print('.', end='')
        print()

print_grid(input_grid, 0)
print()

g = input_grid
for i in range(1, 26):
    g = enhance(g, enhance_array, (i * 6) + 3)
    print(sum(g.values()))
    g = enhance(g, enhance_array, i * 6)
    print(sum(g.values()))
    #print_grid(g, 6)

