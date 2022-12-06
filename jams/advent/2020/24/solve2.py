import sys

# Hex grid moves with cartesian coordinates
moves = {
 'se': (1, -1),
 'sw': (-1, -1),
 'nw': (-1, 1),
 'ne': (1, 1),
 'e': (2, 0),
 'w': (-2, 0)
}

grid = set()

def neighbors(x, y):
    l = set()
    for x2, y2 in moves.values():
        pos = x + x2, y + y2
        l.add(pos)
    return l

def new_state(grid, x, y):
    n = 0
    for g in neighbors(x, y):
        if g in grid:
            n +=1
    if (x, y) in grid:
        return (n == 1) or (n == 2)
    else:
        return n == 2

def step(grid):
    candidates = set()
    for g in grid:
        candidates |= neighbors(*g)
        candidates.add(g)

    ng = {}
    for g in candidates:
        if new_state(grid, *g):
            ng[g] = True
    return ng

def flip_tile(grid, line):
    pos = 0, 0
    while line:
        for k, v in moves.items():
            if line.startswith(k):
                pos = pos[0] + v[0], pos[1] + v[1]
                line = line.removeprefix(k)
    if pos in grid:
        grid.remove(pos)
    else:
        grid.add(pos)

for line in sys.stdin:
    flip_tile(grid, line.strip())
print(len(grid))

for _ in range(100):
    grid = step(grid)
    print(len(grid))
print(len(grid))
