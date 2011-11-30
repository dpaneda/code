#!/usr/bin/python

import sys

def solve(str1, str2, add, delete, swap):
    """Levenshtein distance with some tunning"""
    d = {}
    n, m = len(str1), len(str2)
    for i in xrange(n + 1):
        d[i] = {}
        d[i][0] = i

    for i in xrange(m + 1):
        d[0][i] = i

    for i in xrange(1, n + 1):
        for j in xrange(1, m + 1):
            if (str1[i-1] == str2[j-1]):
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i][j-1] + delete, d[i-1][j] + add, d[i-1][j-1] + swap)
    return d[n][m]

for line in sys.stdin:
    origin, target, costs = line.split()
    add, delete, swap = map(int, costs.split(','))
    print solve(origin, target, add, delete, swap)
