#! /usr/bin/env python
import sys
from dataclasses import dataclass

def step(a, b):
    if a == b:
        return 0
    else:
        return 1 if a < b else -1
 
@dataclass(frozen=True)
class Point:
    x : int
    y : int

    def parse(s):
        return Point(*map(int, s.split(',')))

@dataclass
class Line:
    a : Point
    b : Point

    def parse(s):
        points = s.split(' -> ')
        return Line(*map(Point.parse, points))

    def inner_points(self):
        xstep = step(self.a.x, self.b.x)
        ystep = step(self.a.y, self.b.y)

        p = self.a
        l = [p]
        while p != self.b:
            p = Point(p.x + xstep, p.y + ystep)
            l.append(p)
        return l

lines = map(Line.parse, sys.stdin)

grid = {}

for line in lines:
    for point in line.inner_points():
        grid.setdefault(point, 0)
        grid[point] += 1

count = sum(value > 1 for value in grid.values())
print(count)
