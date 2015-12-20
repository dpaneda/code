#!/usr/bin/python2

import sys
import itertools


def circle(r, c):
    return (2 * r) + (2 * (c - 2))


def is_cell_valid(grid, r, c, y, x):
    if grid[y][x] == '*':
        return True

    for i in xrange(y - 1, y + 2):
        for j in xrange(x - 1, x + 2):
            if i >= 0 and j >= 0 and i < r and j < c and grid[i][j] == '0':
                return True
    return False


def is_grid_valid(grid, r, c):
    for i in range(0, r):
        for j in range(0, c):
            if not is_cell_valid(grid, r, c, i, j):
                return False
    return True


def count_cell(grid, r, c, y, x):
    s = 0
    for i in xrange(y - 1, y + 2):
        for j in xrange(x - 1, x + 2):
            if i >= 0 and j >= 0 and i < r and j < c and grid[i][j] == '*':
                s += 1
    return str(s)


def count_grid(grid, r, c):
    for i in range(0, r):
        for j in range(0, c):
            if grid[i][j] == '.':
                grid[i][j] = count_cell(grid, r, c, i, j)


def clean_grid(grid, r, c):
    start_pending = True
    for i in range(0, r):
        for j in range(0, c):
            if start_pending and grid[i][j] == '0':
                grid[i][j] = 'c'
                start_pending = False
            elif grid[i][j] != '*':
                grid[i][j] = '.'


def copy_grid(grid1, grid2, R, C, r, c):
    offset = (R - r) / 2
    for i in xrange(0, r):
        for j in range(0, c):
            grid2[i + offset][j + offset] = grid1[i][j]


def print_grid(grid, r, c):
    for i in range(0, r):
        print ''.join(grid[i])


def solve():
    R, C, M = map(int, sys.stdin.readline().strip().split())
    big_grid = {}
    grid = {}
    for i in xrange(0, R):
        big_grid[i] = range(0, C)
        for j in range(0, C):
            big_grid[i][j] = '*'

    r, c, m = R, C, M
    while m > circle(r, c):
        m -= circle(r, c)
        r -= 2
        c -= 2

    for i in xrange(0, r):
        grid[i] = range(0, c)
        for j in range(0, c):
            grid[i][j] = '.'

    for p in itertools.product("*.", repeat=circle(r, c)):
        if p.count('*') != m:
            continue

        offset = 0
        for i in range(0, c):
            grid[0][i] = p[i]
        offset += c

        for i in range(0, c):
            grid[r - 1][i] = p[offset + i]
        offset += c

        for i in range(0, r - 2):
            grid[i + 1][0] = p[offset + i]
        offset += r - 2

        for i in range(0, r - 2):
            grid[i + 1][c - 1] = p[offset + i]

        copy_grid(grid, big_grid, R, C, r, c)
        count_grid(big_grid, R, C)
        print
        print_grid(big_grid, R, C)
        if is_grid_valid(big_grid, R, C):
            print
            clean_grid(big_grid, R, C)
            print_grid(big_grid, R, C)
            return

    print 'Impossible'


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    sys.stdout.write("Case #")
    sys.stdout.write(str(case))
    sys.stdout.write(": ")
    solve()
