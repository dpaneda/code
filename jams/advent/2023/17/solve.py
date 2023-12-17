#! /usr/bin/env python

import sys
from dataclasses import dataclass, field
from typing import List
import heapq
from functools import total_ordering
from pprint import pp


def read_grid():
    grid = []
    for line in sys.stdin:
        l = [int(c) for c in line.strip()]
        grid.append(l)
    return grid

@total_ordering
@dataclass(frozen=True)
class State:
    x: int
    y: int
    cost: int
    last_moves : tuple


    def __hash__(self):
        return hash((self.x, self.y, self.last_moves))

    def __eq__(self, other):
        return (self.x == other.x
               and self.y == other.y
               and self.last_moves == other.last_moves)

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        if self.cost == other.cost and (self.x + self.y > other.x + other.y):
            return True
        return False

def add_neighbors(grid, visited, border, s : State) -> List[State]:
    Y = len(grid)
    X = len(grid[0])
    dirs = {
        '^': (0, -1),
        'V': (0, 1),
        '>': (1, 0),
        '<': (-1, 0)
    }

    reverse = {
        '^': 'V',
        'V': '^',
        '>': '<',
        '<': '>'
    }

    for d, v in dirs.items():
        if s.last_moves.count(d) == 3:
            # At most three blocks straight
            continue
        if s.last_moves and s.last_moves[-1] == reverse[d]:
            # Can't go reverse
            continue
        dx, dy = v
        x2, y2 = s.x + dx, s.y + dy
        if x2 < 0 or y2 < 0 or x2 >= X or y2 >= Y:
            continue
        ns = State(
                x2,
                y2,
                s.cost + grid[y2][x2],
                s.last_moves[-2:] + (d,)
        )
        if ns in visited or ns in border:
            continue
#        if ns in border:
#            found = border.index(ns)
#            if ns.cost > border[found].cost:
#                continue
#                print("ERROR")
#                border.pop(found)
#                heapq.heapify(border)
        heapq.heappush(border, ns)

grid = read_grid()
visited = set()
start_state = State(0, 0, 0, tuple())
border = [start_state]
Y = len(grid)
X = len(grid[0])
end = (X - 1, Y - 1)

while border:
    s = heapq.heappop(border)
    #if s in visited:
    #    continue
    if (s.x, s.y) == end:
        print(f"Reach end with cost {s.cost}")
        break
    add_neighbors(grid, visited, border, s)
    #print(s, len(border))
    #pp(border)
    visited.add(s)
