#!/usr/bin/python2

import sys



def path_to(x, y, n):
    if n == 0:
        if (x, y) == (0, 0):
            return ''
        else:
            return 'X'

    if abs(x) > abs(y):
        if x > 0:
            return path_to(x - n, y, n - 1) + 'E'
        else:
            return path_to(x + n, y, n - 1) + 'W'
    else:
        if y > 0:
            return path_to(x, y - n, n - 1) + 'N'
        else:
            return path_to(x, y + n, n - 1) + 'S'

def Solve():
    (dx, dy) = map(int, sys.stdin.readline().strip().split())
    for n in xrange(1, 1000000000):
        path = path_to(dx, dy, n)
        if path[0] != 'X':
            return path

num = int(sys.stdin.readline())
sys.setrecursionlimit(1000000)
for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
