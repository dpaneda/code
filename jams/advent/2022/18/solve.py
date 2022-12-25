#! /usr/bin/env python
import sys

cubes = set()
holes = set()

for line in sys.stdin:
    cube = tuple(map(int, line.split(',')))
    cubes.add(cube)

x_min = min(p[0] for p in cubes)
x_max = max(p[0] for p in cubes)
y_min = min(p[1] for p in cubes)
y_max = max(p[1] for p in cubes)
z_min = min(p[2] for p in cubes)
z_max = max(p[2] for p in cubes)

def get_adjacents(p):
    moves = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]

    x, y, z = p
    for move in moves:
        x2, y2, z2 = move
        p = x + x2, y + y2, z + z2
        yield p

def explore_pocket(p):
    if p in cubes:
        return False

    explored = set()
    explored.add(p)
    frontier = set()
    frontier.add(p)
    
    while frontier:
        new_frontier = set()
        for p in frontier:
            x, y, z = p
            
            if x < x_min or x > x_max:
                return False
            if y < y_min or y > y_max:
                return False
            if z < z_min or z > z_max:
                return False

            for p in get_adjacents(p):
                if p not in cubes and p not in explored:
                    new_frontier.add(p)
                    explored.add(p)
        frontier = new_frontier
    for p in explored:
        holes.add(p)
    return len(explored)

def get_inside_surface():
    sides = 0
    for p in holes:
        x, y, z = p
        for p in get_adjacents(p):
            if p in cubes:
                sides += 1
    return sides

touching = 0

for cube in cubes:
    for p in get_adjacents(cube):
        explore_pocket(p)
        if p in cubes:
            touching += 1

total_surface = 6 * len(cubes) - touching
inside_surface = get_inside_surface()
outside_surface = total_surface - inside_surface
print(f"There are {touching} touching cubes so the total surface is {total_surface}")
print(f"The inside surface is {inside_surface} so the outside surface is {outside_surface}")
