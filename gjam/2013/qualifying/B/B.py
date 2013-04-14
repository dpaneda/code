#!/usr/bin/python2

import sys


def cut_possible(grass, n, m, x, y):
    is_ok = True
    for i in xrange(0, m):
        if grass[x][i] > grass[x][y]:
            is_ok = False
            break

    if is_ok:
        return True

    is_ok = True
    for i in xrange(0, n):
        if grass[i][y] > grass[x][y]:
            is_ok = False
            break

    if is_ok:
        return True


def Solve():
    [n, m] = map(int, sys.stdin.readline().split())

    grass = []
    for i in xrange(0, n):
        grass.append(map(int, sys.stdin.readline().split()))

    for i in xrange(0, n):
        for j in xrange(0, m):
            if not cut_possible(grass, n, m, i, j):
                return 'NO'

    return 'YES'

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
