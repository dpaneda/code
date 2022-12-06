#!/usr/bin/env python3
import sys
total = 0

for line in sys.stdin.readlines():
    mass = int(line)
    total += int(mass / 3) - 2

print(total)
