#!/usr/bin/python2

import sys
import math

def radius(item):
    return item[0]

def height(item):
    return item[1]

def carea(item):
    return math.pi * radius(item) * radius(item)

def harea(item):
    return 2 * math.pi * radius(item) * height(item)

def farea(item):
    return carea(item) + harea(item)

def solve():
    N, K = map(int, raw_input().split())
    pancakes = []
    for i in xrange(0, N):
        r, h = map(int, raw_input().split())
        pancakes.append((r,h))
#    print N, K
#    print pancakes

    max_area = 0
    for i in xrange(0, N):
        p = list(pancakes)
        first = p.pop(i)
        r = radius(first)
        area = farea(first)
        picked = 1
    
        p = sorted(p, key=harea, reverse=True)

        while p:
            pk = p.pop(0)
            if picked == K:
                break
            if radius(pk) > r:
                continue
            picked += 1
            area += harea(pk)

        if area > max_area:
            max_area = area

#    area = math.pi * radius(p[0]) * radius(p[0])
#    area += 2 * math.pi * radius(p[0]) * height(p[0])

#    p2 = sorted(p[1:], key=height, reverse=True)
#    for i in xrange(0, K - 1):
#        area += 2 * math.pi * radius(p2[i]) * height(p2[i])

    return str(max_area)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
