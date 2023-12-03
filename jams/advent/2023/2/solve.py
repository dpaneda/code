#! /usr/bin/env python
import sys
import math
from collections import defaultdict

def read_cubeset(s):
    cubes = {}
    cubeset = (p.split() for p in s.split(', '))
    for n, color in cubeset:
        cubes[color] = int(n)
    return cubes

def valid_cubeset(cubeset):
    bag = read_cubeset('12 red, 13 green, 14 blue')
    return all([bag[color] >= cubeset[color] for color in cubeset.keys()])

def max_cubeset(a, b):
    for color in a.keys():
        b[color] = max(a[color], b[color])
    return b

n = n2 = 0
for line in sys.stdin:
    mincubes = defaultdict(int)
    game, cubesets = line.split(": ")
    gameid = int(game[5:])
    cubesets = list(map(read_cubeset, cubesets.split('; ')))
    
    # Part 1
    if all(map(valid_cubeset, cubesets)):
        n += gameid

    # Part 2
    for cubeset in cubesets:
        mincubes = max_cubeset(cubeset, mincubes)
    n2 += math.prod(mincubes.values())

print(f"1. The sum of the valid gameids is {n}")
print(f"2. The sum of the power of the minimum cubes is {n2}")
