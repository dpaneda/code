#!/usr/bin/python2

import sys


def solve():
    X, R, C = map(int, sys.stdin.readline().split())

    if X > max(R, C):
        return "RICHARD"

    if (R * C) % X:
        return "RICHARD"

    n = X / 2

    if X % 2:
        n += 1

    if n > min(R, C):
        return "RICHARD"

    if X > 3:
        if min(R, C) < 3:
            return "RICHARD"

    if X >= 7:
        # The 7-onimo is the first with holes
        return "RICHARD"

    if X == 5:
        # With 5-ominoes, we need at least 3 x 10 to fix some pieces
        if min(R, C) == 3 and max(R, C) < 10:
            return "RICHARD"

    if X == 6:
        # With 6-ominoes, some pieces are imposible to fix on a 3-narrow grid
        if min(R, C) == 3:
            return "RICHARD"

    return "GABRIEL"


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
