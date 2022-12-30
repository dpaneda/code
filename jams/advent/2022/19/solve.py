#! /usr/bin/env python
import sys
import re
from functools import lru_cache
from enum import IntEnum
from dataclasses import dataclass, replace

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

@dataclass(frozen=True)
class Status():
    minutes: int
    robots: tuple
    rocks: tuple

@lru_cache(maxsize=10000000)
def use_blueprint(bp, needed_robots, status: Status):
    def buildable(robot):
        if robot < Rock.geode and status.robots[robot] >= needed_robots[robot]:
            return False
        if status.minutes >= 24 and robot != Rock.geode:
            return False
        return greater(status.rocks, bp[robot])

    def build(status, robot):
        robots = list(status.robots)
        robots[robot] += 1
        rocks = pay_cost(status.rocks, bp[robot])
        return replace(status, robots=tuple(robots), rocks=rocks)

    def mine(status):
        return replace(status, minutes = status.minutes - 1, rocks=tsum(status.robots, status.rocks))

    best_value = 0
    to_build = list(filter(buildable, range(len(bp)))) 
#    print("ENTER", status, to_build)

    if status.minutes <= 0:
        return status.rocks[Rock.geode]

    status = mine(status)
#    print("MINED", status)
    # Best value just waiting this minute
    best_value = use_blueprint(bp, needed_robots, status) 
    for robot in to_build:
        value = use_blueprint(bp, needed_robots, build(status, robot))
        best_value = max(value, best_value)
    
#    print("LEFT", status)
    return best_value

initial_status = Status(minutes=24, robots=(1,0,0,0),rocks=(0,0,0,0))
initial_status_32 = Status(minutes=32, robots=(1,0,0,0),rocks=(0,0,0,0))
total_quality = 0
total_geodes = 1
for i, line in enumerate(sys.stdin.readlines()):
    bp = read_blueprint(line)
    print(bp)
    needed_robots = tmax(bp)
    value = use_blueprint(bp, needed_robots, initial_status)
    total_quality += (1 + i) * value
    if i <= 3:
        value = use_blueprint(bp, needed_robots, initial_status_32)
        total_geodes *= value
    print(value, total_quality, total_geodes)
print(f"Total quality is {total_quality} and total_geodes (part 2 ) is {total_geoges}")
