#!/usr/bin/python2

import sys


def int2base(x, base, digs):
    if x == 0:
        return digs[0]
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    digits.reverse()
    return ''.join(digits)


def solve():
    L, n = sys.stdin.readline().split()
    n = int(n)
    digits = 1
    while n > len(L) ** digits:
        n -= len(L) ** digits
        digits += 1
    label = int2base(n - 1, len(L), L)
    while len(label) < digits:
        label = L[0] + label
    return label

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, solve())
