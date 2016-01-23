#!/usr/bin/python2

import sys
import math
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Segment = namedtuple('Segment', ['a', 'b'])

def distance(pos, pos2):
    sq1 = (pos.x - pos2.x) * (pos.x - pos2.x)
    sq2 = (pos.y - pos2.y) * (pos.y - pos2.y)
    return math.sqrt(sq1 + sq2)

def Solve():
    lines = int(raw_input())
    stars = []
    for i in xrange(0, lines):
        pair = map(int, raw_input().split())
        stars.append(Point(*pair))

    distances = {}
    l = len(stars)
    for i in xrange(0, l):
        for j in xrange(i + 1, l):
            a = stars[i]
            b = stars[j]
            d = distance(a, b)
            if d not in distances:
                distances[d] = []
            distances[d].append(Segment(a, b))

    boomerangs = 0

    for k in distances:
        l = distances[k]
        n = len(l)
        for i in xrange(0, n):
            for j in xrange(i + 1, n):
                s1 = l[i]
                s2 = l[j]
                if s1.a in s2 or s1.b in s2:
                    boomerangs += 1
    return boomerangs

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
