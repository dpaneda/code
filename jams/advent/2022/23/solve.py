#! /usr/bin/env python
import sys
import time
from collections import OrderedDict, defaultdict

moves = OrderedDict()
moves[( 0, -1)] = ((-1, -1), (0, -1), (1, -1))
moves[( 0,  1)] = ((-1,  1), (0,  1), (1,  1))
moves[( -1, 0)] = ((-1, -1), (-1, 0), (-1, 1))
moves[(  1, 0)] = (( 1, -1), ( 1, 0), ( 1, 1))

def min_rectangle(grid):
    x_min = min(p[0] for p in grid)
    x_max = max(p[0] for p in grid)
    y_min = min(p[1] for p in grid)
    y_max = max(p[1] for p in grid)

    spaces = ((x_max - x_min + 1) * (y_max - y_min + 1)) - len(grid)

    print(f"The rectangle is ({y_min}, {x_min}) - ({y_max}, {x_max}) and there are {spaces} spaces and {len(grid)} elves")
    return spaces, x_min, y_min, x_max, y_max

def print_grid(grid):
    _, x1, y1, x2, y2 = min_rectangle(grid)
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if (x, y) in grid:
                print('#', end='')
            else:
                print('.', end='')
        print()


def expand(grid):
    def alone(p):
        x, y = p
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                p2 = x + dx, y + dy
                if p2 in grid:
                    return False
        return True

    def valid_move(p, move):
        x, y = p
        for dx, dy in moves[move]:
            if (x + dx, y + dy) in grid:
                return False
        return True

    proposals = defaultdict(list)

    for p in grid:
        if alone(p):
            continue
        for move in moves:
            if valid_move(p, move):
                x, y = p
                dx, dy = move
                destiny = (x + dx, y + dy)
                proposals[destiny].append(p)
                break

    if not proposals:
        return False

    for p, v in proposals.items():
        if len(v) > 1:
            continue
        grid.remove(v.pop())
        grid.add(p)

    k, v = moves.popitem(0)
    moves[k] = v
    return True

elves = set()

y = 0
for line in sys.stdin:
    for x in range(0, len(line)):
        if line[x] == '#':
            elves.add((x, y))
    y += 1

for i in range(1, 10000):
#    print_grid(elves)
#    time.sleep(0.01)
    if i == 10: 
        print("Status at round 10")
        print_grid(elves)
    if not expand(elves):
        print(f"Stable status at round {i}")
        break
        print_grid(elves)
