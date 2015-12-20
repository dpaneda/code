#!/usr/bin/python2

import sys

num = int(sys.stdin.readline())

hs = map(int, sys.stdin.readline().split())

be = 0

for i in xrange(0, 10 ** 5):
    be = i
    for h in hs:
        if h > be:
            be -= (h - be)
        else:
            be += (be - h)

        if be < 0:
            break
    if be >= 0:
        break

print(i)
