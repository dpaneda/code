#!/usr/bin/python2

import sys


def solve():
    sys.stdin.readline()
    naomi = map(float, sys.stdin.readline().strip().split())
    ken = map(float, sys.stdin.readline().strip().split())
    naomi.sort()
    ken.sort()
    deceitful = 0
    war = 0

    n = list(naomi)
    k = list(ken)
    while n:
        if n[0] < k[0]:
            k.pop()
        else:
            k.pop(0)
            deceitful += 1
        n.pop(0)

    while naomi:
        if naomi[-1] > ken[-1]:
            war += 1
        else:
            ken.pop()
        naomi.pop()
    return deceitful, war

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    d, w = solve()
    print "Case #%d: %d %d" % (case, d, w)
