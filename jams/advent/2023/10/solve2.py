#! /usr/bin/env python

import sys
from collections import defaultdict

# Delta of the exits as (dx, dy)
exits = {
    '|':((0, -1), (0, 1)),
    '-':((-1, 0), (1, 0)),
    'L':((0, -1), (1, 0)),
    'J':((0, -1), (-1, 0)),
    '7':((0, 1), (-1, 0)),
    'F':((0, 1), (1, 0)),
}

def print_tiles(tiles, N, M):
    DISPLAY_SHAPES = {
        '.': '.',
        ':': '░',
        '\n': '',
        '|': '│',
        '-': '─',
        'L': '└',
        'J': '┘',
        '7': '┐',
        'F': '┌',
        'S': '▆',
    }

    for y in range(-1, N):
        for x in range(-1, M):
            p = x, y
            c = tiles[p]
            print(DISPLAY_SHAPES[c], end='')
        print()

def fill_grid(grid, tiles):
    """Fill exits for each tile"""
    start = None
    for p, c in tiles.items():
        if c == 'S':
            start = p
        for dx, dy in exits.get(c, []):
            a = p
            b = p[0] + dx, p[1] + dy
            grid[a].add(b)

    # Add exists for the start
    for p, c in tiles.items():
        for (dx, dy) in exits.get(c, []):
            a = p
            b = p[0] + dx, p[1] + dy
            if b == start:
                grid[b].add(a)
    return start

def fill_gaps(grid, tiles):
    """Create pipes on empty places with exits on both
    sides, either vertical or horizontal
    """
    for p, c in tiles.items():
        u = p[0], p[1] - 1
        d = p[0], p[1] + 1
        e = p[0] - 1, p[1]
        w = p[0] + 1, p[1]
        if p in grid[u] | grid[d]:
            tiles[p] = '|'
        if p in grid[e] | grid[w]:
            tiles[p] = '-'

def flood(tiles):
    """Flood everything from the outside"""
    visited = set()
    border = set([(0, 0)])
    while border:
        new_border = set()
        for p in border:
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                p2 = p[0] + dx, p[1] + dy
                if tiles.get(p2, None) == '.' and p2 not in visited:
                    new_border.add(p2)
        visited |= border
        border = new_border
    for p in visited:
        tiles[p] = ':'

def enclosed(tiles):
    def even(x):
        return x % 2 == 0

    enclosed = [1 for p, c in tiles.items() if all(map(even, p)) and c == '.']
    return len(enclosed)


# The grid is a dictionary of sets which contains the exits
grid = defaultdict(set)

# The axis grow to the right and down (non-standard but convenient)
lines = sys.stdin.readlines()

tiles = defaultdict(lambda: '.')
# Expand the tiles to add spaces to be able to flood properly
N = len(lines)
M = len(lines[0])
for y in range(N):
    for x in range(M):
        p = x*2, y*2
        tiles[p] = lines[y][x]

N, M = (N * 2), (M * 2)

print("Expanded map")
start = fill_grid(grid, tiles)
print_tiles(tiles, N, M)

fill_gaps(grid, tiles)
print("Expanded map after closing the gaps")
print_tiles(tiles, N, M)

# Call fill grid to add the added gaps to the grid
start = fill_grid(grid, tiles)

visited = set()
border = set([start])
while border:
    new_border = set()
    for p in border:
        for p2 in grid[p]:
            if p2 not in visited:
                new_border.add(p2)
    visited |= border
    border = new_border

# Clean everything but the main loop
for p in tiles:
    if p not in visited:
        tiles[p] = '.'
print("Expanded map only with the main loop")
print_tiles(tiles, N, M)

flood(tiles)
print("Final flooded map")
print_tiles(tiles, N, M)

print(f"The number of tiles enclosed by the loop is {enclosed(tiles)}")
