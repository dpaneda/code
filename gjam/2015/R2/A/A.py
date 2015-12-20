#!/usr/bin/python2

import sys


def ok_dir(grid, i, j, d):
    try:
        while True:
            if d == '^':
                i -= 1
            elif d == '>':
                j += 1
            elif d == 'v':
                i += 1
            elif d == '<':
                j -= 1

            if i < 0 or j < 0:
                return False

            if grid[i][j] != '.':
                return True
    except IndexError:
        return False

    return False


def ok_cell(grid, i, j):
    if grid[i][j] == '.':
        return 0

    if ok_dir(grid, i, j, grid[i][j]):
        #print "OK", i, j
        return 0

    #print "NOK", i, j
    dirs = "^>v<"

    for d in dirs:
        okd = ok_dir(grid, i, j, d)
        if okd:
            return 1
    return -1


def solve():
    R, C = map(int, sys.stdin.readline().split())
    grid = []
    for _ in xrange(R):
        grid.append(sys.stdin.readline().strip())

    #for g in grid:
    #    print g
    changes = 0
    for i in xrange(R):
        for j in xrange(C):
            ok = ok_cell(grid, i, j)
            if ok >= 0:
                changes += ok
            else:
                return "IMPOSSIBLE"

    return changes

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
