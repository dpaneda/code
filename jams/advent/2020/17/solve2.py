import sys

grid = set()
y = 0

for line in sys.stdin:
    for x in range(len(line)):
        if line[x] == '#':
            grid.add((x, y, 0, 0))
    y += 1

def neighbors(x, y, z, w):
    l = set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for o in range(w-1, w+2):
                    l.add((i, j, k, o))
    l.remove((x, y, z, w))
    return l

def new_state(grid, x, y, z, w):
    n = 0
    for g in neighbors(x, y, z, w):
        if g in grid:
            n +=1
    if n == 3:
        return True
    else:
        return n == 2 and (x, y, z, w) in grid

def step(grid):
    candidates = set()
    for g in grid:
        candidates |= neighbors(*g)
        candidates.add(g)

    ng = set()
    for g in candidates:
        if new_state(grid, *g):
            ng.add(g)
    return ng

for _ in range(10):
    grid = step(grid)
print(len(grid))
