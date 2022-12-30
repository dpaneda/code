#! /usr/bin/env python
import sys, math
from collections import defaultdict
from dataclasses import dataclass

storms_status = []

lines = sys.stdin.readlines()
N = len(lines) - 2
M = len(lines[0]) - 3
start = (0, -1)
end = (M - 1, N)
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
        for storm in storms_status:
            if storm == new_storms:
                return i + 1
        storms_status.append(new_storms)

def print_storms(storms_status, i):
    print(f"---Iteration {i} ---Looping at {LOOP_AT}------------")
    i = i % LOOP_AT
    x_min = min(p[0] for p in storms_status[0])
    y_min = min(p[1] for p in storms_status[0])
    x_max = max(p[0] for p in storms_status[0])
    y_max = max(p[1] for p in storms_status[0])
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            p = x, y
            if p in storms_status[i]:
                to_print = storms_status[i][p]
                if len(to_print) > 1:
                    to_print = len(to_print)
            else:
                to_print = '.'
            print(to_print, end='')
        print()
    
LOOP_AT = simulate(storms_status)
#import time
#for i in range(100):
#    print_storms(storms_status, i)
#    time.sleep(0.3)
#sys.exit(0)

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
                s2 = Status(p[0], p[1], s.minute + 1, s.start, s.end)
                #if better_status(s2, current_status):
                #    continue
                if s2.is_end(p):
                    print(f"The end is here {s2}")
                    return s.minute
                else:
                    new_status.add(s2)
    return new_status

@dataclass(frozen=True, eq=True)
class Status:
    x: int
    y: int
    minute: int
    start: tuple
    end: tuple

    def valid(self, p):
        x, y = p
        if p == self.start or p == self.end:
            return True
        if not 0 <= x < M:
            return False
        if not 0 <= y < N:
            return False
        return True

    def is_end(self, p):
        return p == self.end

    def adjacents(self):
        x, y = self.x, self.y
        l = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
            (x, y)
        ]
        return filter(self.valid, l)

current_status = set()
current_status.add(Status(start[0], start[1], 0, start, end))
frontier_status = current_status

while frontier_status:
    frontier_status = status_step(frontier_status, current_status, storms_status)
    if type(frontier_status) == int:
        break

current_status = set()
current_status.add(Status(end[0], end[1], frontier_status, end, start))
frontier_status = current_status
while frontier_status:
    frontier_status = status_step(frontier_status, current_status, storms_status)
    if type(frontier_status) == int:
        break

current_status = set()
current_status.add(Status(start[0], start[1], frontier_status, start, end))
frontier_status = current_status
while frontier_status:
    frontier_status = status_step(frontier_status, current_status, storms_status)
    if type(frontier_status) == int:
        break
