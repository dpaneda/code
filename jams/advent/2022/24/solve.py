#! /usr/bin/env python
import sys, math
from collections import defaultdict
from dataclasses import dataclass

storms_status = []

lines = sys.stdin.readlines()
N = len(lines) - 2
M = len(lines[0]) - 3
start = (0, -1)
end = (N - 1, N)
#start = (0, lines[0].index('.'))
#end = (lines[-1].index('.'), N - 1)

# Clean walls
lines.pop()
lines.pop(0)

storms = defaultdict()
for y, line in enumerate(lines):
    for x, v in enumerate(line.strip('#\n')):
        if v != '.':
            storms[(x, y)] = v
storms_status.append(storms)

print(f"Going from {start} to {end}, through {len(storms)} storms. The storm cage is {M} x {N}")

def move_storm(p, v):
    x, y = p
    match v:
        case '^': y -= 1
        case 'v': y += 1
        case '<': x -= 1
        case '>': x += 1
    return x % M, y % N

def move_storms(storms):
    moved_storms = defaultdict(str)
    for p, v in storms.items():
        for c in v:
            p2 = move_storm(p, c)
            moved_storms[p2] += c
    return moved_storms

def simulate(storms_status):
    for i in range(10000):
        new_storms = move_storms(storms_status[-1])
        for j, storm in enumerate(storms_status):
            if storm == new_storms:
                return i
        storms_status.append(new_storms)

LOOP_AT = simulate(storms_status)

def better_status(s, current_status):
    for s2 in current_status:
        if (s.x, s.y) == (s2.x, s2.y) and s2.minute + LOOP_AT <= s.minute:
            #print(f"Already present and better {s} {s2}")
            return True
    return False

def status_step(frontier_status, current_status, storms_status):
    new_status = set()
    for s in frontier_status:
        for p in s.adjacents():
            if p not in storms_status[(s.minute + 1) % LOOP_AT]:
                s2 = Status(p[0], p[1], s.minute + 1)
                if better_status(s2, current_status):
                    continue
                if Status.is_end(*p):
                    print(f"The end is here {s2}")
                else:
                    new_status.add(s2)
    return new_status

@dataclass(frozen=True, eq=True)
class Status:
    x: int
    y: int
    minute: int

#    def __eq__(self, other):
#        if self.x != other.x:
#            return False
#        if self.y != other.y:
#            return False
#        if self.minute % LOOP_AT != other.minute % LOOP_AT:
#            return False
#        return True

    def valid(p):
        x, y  = p
        if Status.is_end(x, y) or (x, y) == (0, -1):
            return True
        if not 0 <= x < M:
            return False
        if not 0 <= y < N:
            return False
        return True

    def is_end(x, y):
        return (x, y) == end

    def adjacents(self):
        x, y = self.x, self.y
        l = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x, y)
        ]
        return filter(Status.valid, l)

current_status = set()
current_status.add(Status(0, -1, 0))
frontier_status = current_status

while frontier_status:
    frontier_status = status_step(frontier_status, current_status, storms_status)
    print("----")
    print(frontier_status)
