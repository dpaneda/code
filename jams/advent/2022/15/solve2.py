#! /usr/bin/env python
import sys
import re
from dataclasses import dataclass

def manhattan(a, b):
    return sum(abs(v1-v2) for v1, v2 in zip((a.x, a.y), (b.x, b.y)))

@dataclass(frozen=True,eq=True)
class Point:
    x: int
    y: int

@dataclass
class Sensor:
    pos: Point
    distance: int

    def in_radio(self, p):
        distance = manhattan(self.pos, p)
        return distance <= self.distance

    def frontier(self):
        distance = self.distance + 1
        x, y = self.pos.x, self.pos.y
        for i in range(0, distance + 1):
            yield Point(x + i, y - distance + i) # north -> west
            yield Point(x - i, y - distance + i) # north -> east
            yield Point(x + i, y + distance - i) # south -> west
            yield Point(x - i, y + distance - i) # south -> east
        return

beacons = set()
sensors = []

for line in sys.stdin:
    m = re.search("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
    sensor_pos = Point(int(m[1]), int(m[2]))
    beacon = Point(int(m[3]), int(m[4]))
    distance = manhattan(sensor_pos, beacon)
    s = Sensor(sensor_pos, distance)
    beacons.add(beacon)
    sensors.append(s)

def free_space(p):
    for s in sensors:
        if s.in_radio(p):
            return False
    return True

def in_area(p):
    return 0 <= p.x <= 4000000 and 0 <= p.y <= 4000000

for sensor in sensors:
    for p in sensor.frontier():
        if free_space(p) and in_area(p):
            print(p)
            print(p.x * 4000000 + p.y)
            sys.exit(0)
