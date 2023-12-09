#! /usr/bin/env python
import sys
import re
from functools import lru_cache
from enum import IntEnum

def read_blueprint(line):
    bp = [0] * 4
    for robot, n, rock in re.findall("Each (\w+) robot costs (\d+) (\w+)", line):
        costs = [0] * 4
        costs[Rock[rock]] = int(n)
        bp[Rock[robot]] = tuple(costs)
    for robot, n1, r1, n2, r2 in re.findall("Each (\w+) robot costs (\d+) (\w+) and (\d+) (\w+)", line):
        costs = [0] * 4
        costs[Rock[r1]] = int(n1)
        costs[Rock[r2]] = int(n2)
        bp[Rock[robot]] = tuple(costs)
    return tuple(bp)

def greater(a, b):
#    if a[0] < b[0] or a[1] < b[1] or a[2] < b[2]:
#        return False
#    return a[3] >= b[3]

    for i, n in enumerate(b):
        if a[i] < n:
            return False
    return True

def pay_cost(a, b):
    l = [i - j for i, j in zip(a, b)]
    return tuple(l)

def tsum(a, b):
    return tuple(map(sum, zip(a, b)))

def tmax(l):
    return tuple(map(max, zip(*l)))

Rock = IntEnum('Rock', ['ore', 'clay', 'obsidian', 'geode'], start=0)

@lru_cache(maxsize=10000000)
def use_blueprint(bp, needed_robots, minutes, robots, rocks):
#    print("ENTER", minutes, robots, rocks)

    if minutes <= 0:
        return rocks[Rock.geode]

    new_rocks = tsum(robots, rocks) # mine

#    print("MINED", minutes, robots, rocks)
    # Best value just waiting this minute
    best_value = use_blueprint(bp, needed_robots, minutes - 1, robots, new_rocks)
    for robot in (0, 1, 2, 3):
        if robots[robot] >= needed_robots[robot] and robot < Rock.geode:
            continue
        if not greater(rocks, bp[robot]):
            continue
        robots2 = list(robots)
        robots2[robot] += 1
        value = use_blueprint(bp, needed_robots, minutes - 1, tuple(robots2), pay_cost(new_rocks, bp[robot]))
        best_value = max(value, best_value)
    
#    print("LEFT", minutes, robots, rocks)
    return best_value

#robots=(1,0,0,0)
#rocks=(0,0,0,0)
total_quality = 0
total_geodes = 1
for i, line in enumerate(sys.stdin.readlines()):
    bp = read_blueprint(line)
    print(bp)
    robots=(1,0,0,0)
    rocks=(0,0,0,0)
    needed_robots = tmax(bp)
    value = use_blueprint(bp, needed_robots, 24, robots, rocks)
    total_quality += (1 + i) * value
    print(f"Total quality so far is {total_quality}, last value is {value}")
    if i <= -3:
        robots=(1,0,0,0)
        rocks=(0,0,0,0)
        value = use_blueprint(bp, needed_robots, 32, robots, rocks)
        total_geodes *= value
    print(f"Total geodes so far are {total_geodes}")
print(f"Total quality is {total_quality} and total_geodes (part 2) is {total_geodes}")
