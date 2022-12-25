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

for s in sensors:
    print(s)

#y = 2000000
c = 0

for x in range(0, 20):
  for y in range(0, 20):
    for s in sensors:
        p = Point(x, y)
        if s.in_radio(p) and p not in beacons:
            c += 1
            break
        else:
            print(p)
sys.exit()
for x in range(-5192750, 9016653):
    for s in sensors:
        p = Point(x, y)
        if s.in_radio(p) and p not in beacons:
            c += 1
            break
print(c)
