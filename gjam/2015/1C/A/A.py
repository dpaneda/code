#!/usr/bin/python2

import sys


def solve():
    R, C, W = map(int, sys.stdin.readline().split())

    hits = (C / W) * R
    hits += (W - 1)
    if (C % W):
        hits += 1
    return hits

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
