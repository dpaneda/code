#! /usr/bin/env python

import sys
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Vector:
    x: int = 0
    y: int = 0

@dataclass(frozen=True)
class Beam:
    v: Vector
    x: int
    y: int

UP    = Vector(y=-1)
DOWN  = Vector(y=1)
LEFT  = Vector(x=-1)
RIGHT = Vector(x=1)


bounces = {
    '/': {
        UP: RIGHT,
        DOWN: LEFT,
        RIGHT: UP,
        LEFT: DOWN,
    },
    '\\': {
        UP: LEFT,
        DOWN: RIGHT,
        RIGHT: DOWN,
        LEFT: UP,
    }
}

splits = {
    '|': {
        UP: [UP],
        DOWN: [DOWN],
        RIGHT: [UP, DOWN],
        LEFT: [UP, DOWN],
    },
    '-': {
        UP: [LEFT, RIGHT],
        DOWN: [LEFT, RIGHT],
        RIGHT: [RIGHT],
        LEFT: [LEFT],
    }
}

def collide(v : Vector, what) -> List[Vector]:
    match what:
        case '.':
            return [v]
        case '/' | '\\':
            return [bounces[what][v]]
        case '|' | '-':
            return splits[what][v]

def step(beams) -> List[Beam]:
    global grid
    Y = len(grid)
    X = len(grid[0])

    next_beams = set()
    for beam in beams:
        what = grid[beam.y][beam.x]
        for v in collide(beam.v, what):
            b = Beam(v, beam.x + v.x, beam.y + v.y)
            if 0 <= b.x < X and 0 <= b.y < Y:
                next_beams.add(b)
    return next_beams


def energized_grid(grid, energized):
    for y in range(X):
        for x in range(X):
            if (x, y) in energized:
                print('#', end='')
            else:
                print(grid[y][x], end ='')
        print()

def energize(grid, beam):
    beams = set([beam])
    energized = set()

    # Ugly and slow
    for _ in range(1400):
        for b in beams:
            energized.add((b.x, b.y))
        beams = step(beams)
    print(f"Energized for beam {beam}: {len(energized)}")
    return len(energized)


grid = []
for line in sys.stdin:
    grid.append(line.strip())

Y = len(grid)
X = len(grid[0])

max_energized = 0

for y in range(Y):
    n = energize(grid, Beam(RIGHT, 0, y))
    max_energized = max(max_energized, n)
    n = energize(grid, Beam(LEFT, X - 1, y))
    max_energized = max(max_energized, n)

for x in range(X):
    n = energize(grid, Beam(DOWN, x, 0))
    max_energized = max(max_energized, n)
    n = energize(grid, Beam(UP, x, Y - 1))
    max_energized = max(max_energized, n)

print(max_energized)
