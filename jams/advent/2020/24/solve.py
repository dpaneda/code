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
