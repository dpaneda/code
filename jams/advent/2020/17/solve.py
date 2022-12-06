import sys

grid = {}
y = 0

for line in sys.stdin:
    for x in range(len(line)):
        if line[x] == '#':
            grid[(x, y, 0)] = True
    y += 1

def neighbors(x, y, z):
    l = set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                l.add((i, j, k))
    l.remove((x, y, z))
    return l

def new_state(grid, x, y, z):
    n = 0
    for g in neighbors(x, y, z):
        if g in grid:
            n +=1
    if n == 3:
        return True
    else:
        return n == 2 and (x, y, z) in grid

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


for _ in range(6):
    grid = step(grid)
print(len(grid))
