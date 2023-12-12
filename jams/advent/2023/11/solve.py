#! /usr/bin/env python

import sys
from functools import partial

universe = [s.strip() for s in sys.stdin.readlines()]

EXPAND_FACTOR = 1000000 - 1 # Change this to get part 1 or 2

def expanded_indexes(l):
    def empty(l):
        return all(map(lambda c : c =='.', l))

    is_expanded = [empty(k) for k in l]
    return [i for i, v in enumerate(is_expanded) if v]

def get_galaxies(universe):
    expanded_rows = expanded_indexes(universe)
    expanded_columns = expanded_indexes(zip(*universe))

    galaxies = set()
    for y, row in enumerate(universe):
        for x, c in enumerate(row):
            if c != '#':
                continue
            dx = sum(EXPAND_FACTOR * (i < x) for i in expanded_columns)
            dy = sum(EXPAND_FACTOR * (i < y) for i in expanded_rows)
            p = x + dx, y + dy
            galaxies.add(p)
    return galaxies

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

galaxies = get_galaxies(universe)
n = 0
for g1 in galaxies:
    for g2 in galaxies:
        n += distance(g1, g2)
print(n // 2)

