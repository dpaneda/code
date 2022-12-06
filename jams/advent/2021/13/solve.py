#! /usr/bin/env python
import sys
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x : int
    y : int

    def yfold(self, n):
        if self.y < n:
            return None
        else:
            y = n - (self.y - n)
            return Point(self.x, y)

    def xfold(self, n):
        if self.x < n:
            return None
        else:
            x = n - (self.x - n)
            return Point(x, self.y)

grid = set()

def fold(grid, axis, n):
    print(f"Fold on {axis} and {n}")
    add = set()
    remove = set()
    for p in grid:
        if axis == 'x':
            p2 = p.xfold(n)
        else:
            p2 = p.yfold(n)
        if p2:
            remove.add(p)
            add.add(p2)
    for p in add:
        grid.add(p)
    for p in remove:
        grid.remove(p)

for line in sys.stdin:
    match line.strip().split(','):
        case [x, y]:
            grid.add(Point(int(x), int(y)))
        case [sfold] if sfold:
            where = sfold.split(' ')[-1]
            axis, n = where.split('=')
            fold(grid, axis, int(n))
print(len(grid))

for y in range(0, 6):
    for x in range(0, 80):
        if Point(x, y) in grid:
            print('#', end='')
        else:
            print(' ', end='')
    print()

