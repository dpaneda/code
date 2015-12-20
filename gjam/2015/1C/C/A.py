#!/usr/bin/python2

import sys


def solve():
    _, audience = sys.stdin.readline().split()

    friends = 0
    current = 0
    for p in xrange(len(audience)):
        if current < p:
            needed = p - current
            friends += needed
            current += needed
        current += int(audience[p])

    return friends

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
