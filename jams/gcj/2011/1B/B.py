#!/usr/bin/python
# Obviusly a work in progress

import sys

def Solve():
    [c, d] = map(int, sys.stdin.readline().split())
    street = {}
    for vendor in range(0, c):
        [p, v] = map(int, sys.stdin.readline().split())
        street[p] = v
        
    return str(lenght)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: " + Solve()
