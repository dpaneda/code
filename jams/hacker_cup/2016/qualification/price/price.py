#!/usr/bin/python2

import sys

def Solve():
    N, P = map(int, raw_input().split())
    boxes = map(int, raw_input().split())

    a = b = 0
    s = 0
    r = 0

    for b in xrange(0, N):
        s += boxes[b]

        while s > P and a < b:
            s -= boxes[a]
            a += 1

        if s <= P:
            r += (b - a) + 1

    return r

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
