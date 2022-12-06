#! /usr/bin/env python
import sys

elfs = []

calories = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if len(line):
        calories += int(line.strip())
    else:
        elfs.append(calories)
        calories=0

elfs.sort()

print(elfs[-1])
print(sum(elfs[-3:]))
