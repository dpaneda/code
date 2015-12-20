#!/usr/bin/python2

import sys


def get_max(grid, n, m, x, y, turned=None):
    if x >= m or y >= n or x < 0 or y < 0:
        return 0
    if grid[y][x] == '#':
        return 0

    res = []
    if turned == 'up' and y > 0:
        res.append(get_max(grid, n, m, x, y - 1, turned))
    elif turned == 'left' and x > 0:
        res.append(get_max(grid, n, m, x - 1, y, turned))
    elif turned != 'off':
        res.append(get_max(grid, n, m, x, y - 1, 'up'))
        res.append(get_max(grid, n, m, x - 1, y, 'left'))

    if turned in ('up', 'left'):
        turned = 'off'
    res.append(get_max(grid, n, m, x, y + 1, turned))
    res.append(get_max(grid, n, m, x + 1, y, turned))
    res.append(get_max(grid, n, m, x + 1, y + 1, turned))

    print x, y, turned, max(res)
    return 1 + max(res)


def path_len(grid, a, b, c, d):
    if a == c and b == d:
        return 1
    paths = []
    if a < c and grid[b][a + 1] != '#':
        paths.append(path_len(grid, a + 1, b, c, d))
    if b < d and grid[b + 1][a] != '#':
        paths.append(path_len(grid, a, b + 1, c, d))
    if not paths:
        return 1
    return 1 + max(paths)


def path_exists(grid, a, b, c, d):
    """ Is there a path between a,b  and c,d ?"""
    total = c + d - a - b + 1
    return total == path_len(grid, a, b, c, d)


def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for i in xrange(0, n):
        grid.append(sys.stdin.readline().strip())

    for i in xrange(0, n):
        print grid[i]

    max_path = path_len(grid, 0, 0, m - 1, n - 1)
    for a in xrange(0, m):
        for b in xrange(1, n):
            c = a
            for d in xrange(0, b):
                if path_exists(grid, 0, 0, a, b):
                    path1 = path_len(grid, 0, 0, a, b)
                    path2 = b - d - 1
                    path3 = path_len(grid, c, d, m - 1, n - 1)
                    #print a, b, c, d
                    #print path1
                    #print path2
                    #print path3
                    new_path = path1 + path2 + path3
                    if new_path > max_path:
                        max_path = new_path
    return max_path

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, solve())
