#!/usr/bin/python2

import sys


def count_blacks(grid):
    blacks = 0
    for line in grid:
        blacks += line.count('#')
    return blacks


def check_square(grid):
    for b in xrange(0, len(grid)):
        a = grid[b].find('#')
        if a >= 0:
            break

    size = grid[b].count('#')

    for y in xrange(b, b + size):
        for x in xrange(a, a + size):
            if grid[y][x] != '#':
                return 0
    return size


def Solve():
    lines = int(sys.stdin.readline())
    grid = []
    for i in xrange(0, lines):
        grid.append(sys.stdin.readline().strip())

    blacks = count_blacks(grid)
    size = check_square(grid)

    if size * size == blacks:
        return "YES"
    else:
        return "NO"

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
