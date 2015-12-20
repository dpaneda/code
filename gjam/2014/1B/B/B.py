#!/usr/bin/python2

import sys
import math


def count0(n):
    return list(bin(n)).count('1') - 1


def solve():
    A, B, K = map(int, sys.stdin.readline().split())

    wins = 0
    for a in xrange(0, A):
        for b in xrange(0, B):
            if a & b < K:
#                print a, b
                wins += 1

    asize = int(math.log(A) / math.log(2))
    bsize = int(math.log(B) / math.log(2))
    ksize = int(math.log(K) / math.log(2))

    csize = min(asize, bsize, ksize)
    dsize = max(0, min(asize, bsize) - ksize)
    esize = max(0, max(asize, bsize) - min(asize, bsize))

    A2 = 2 ** asize
    B2 = 2 ** bsize
    K2 = 2 ** ksize

    print A, A2
    print B, B2
    print K, K2

    combs = pow(pow(2, csize), 2) * pow(3, dsize) * pow(2, esize)

    for a in xrange(A2, A):
        for b in xrange(B2, B):
            if a & b < K:
                combs += 1

    print combs

    return wins

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, solve())
