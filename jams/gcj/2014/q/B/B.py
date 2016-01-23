#!/usr/bin/python2

import sys


def solve():
    C, F, X = map(float, sys.stdin.readline().strip().split())
    seconds = 0
    cps = 2
    while True:
        without_farm = X / cps
        with_farm = (C / cps) + (X / (cps + F))
        if with_farm <= without_farm:
            seconds += C / cps
            cps += F
        else:
            return seconds + without_farm

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #%d: %.7f " % (case, solve())
