#!/usr/bin/python2

import sys
import random

def solve():
    N = input()
    W = map(int, raw_input().split())

    #N = 100
    #W = []
    #for _ in xrange(N):
    #    W.append(random.randint(0, 1000))
    #print W

    cache = {}
    sys.setrecursionlimit(1000000)

    def best(pos, size, total):
        if pos >= N:
            return size

        if pos in cache:
            return cache[pos]

        if 6 * W[pos] < total:
            args = (pos + 1, size, total)
            return best(*args)

        args1 = (pos + 1, size + 1, total + W[pos])
        args2 = (pos + 1, size, total)
        cache[pos+1] = max(best(*args1), best(*args2))

        return cache[pos+1]

    return best(0, 0, 0)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
