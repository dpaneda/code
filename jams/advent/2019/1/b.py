#!/usr/bin/env python3
import sys
total = 0

for line in sys.stdin.readlines():
    mass = int(line)
    fuel = int(mass / 3) - 2
    while fuel > 0:
        total += fuel
        fuel = int(fuel / 3) - 2

print(total)
