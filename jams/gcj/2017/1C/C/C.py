#!/usr/bin/python2

import sys


def equals(P):
    for i in xrange(0, len(P)):
        if (P[0] - P[i]) > 0.00000001:
            return False
    return True

def diff(P):
    a = P[0]
    n = 1
    for i in xrange(1, len(P)):
        if P[i] == a:
            n += 1
        else:
            return n, P[i] - a


def solve():
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    P = map(float, raw_input().split())
    P.sort()

    while U > 0:
        if N == 1:
            P[0] += U
            break

        if equals(P):
            u = U / len(P)
            for i in xrange(0, len(P)):
                P[i] += u
            break
        n, u = diff(P)
        if (u * n) < U:
            for i in xrange(0, n):
                P[0] += u
            U -= u * n
            P.sort()
            print P
        else:
            for i in xrange(0, n):
                P[i] += U / n
            break

    p = 1
    for i in xrange(0, len(P)):
        p *= P[i]
    return str(p)



num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
