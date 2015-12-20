#!/usr/bin/python

import sys
import math


def solve():
    p, q = map(int, sys.stdin.readline().split('/'))

    if (((2 ** 40) * p) % q != 0):
        return "impossible"

    return max(1, int(math.ceil(math.log2(q / p))))


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print("Case #%d: %s" % (case, solve()))
