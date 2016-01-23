#!/usr/bin/python2

import sys

s = 0

for i in xrange(1, 100, 2):
    s += 2 * i - 1
    print(s)


def Solve():
    (r, t) = map(int, sys.stdin.readline().split())
    circle = r + 1
    painted = 0
    s = 0
    while True:
        n = (2 * circle) - 1
        s += n
        print(s)
        t -= n
        if t >= 0:
            painted += 1
            circle += 2
        else:
            break
    return painted

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
