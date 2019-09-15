#!/usr/bin/python2

import sys
import operator

def percent(N, l):
    p = 0
    for n in l:
        p += round((100. * n) / N)
    return int(p)

def deltas(N, l):
    d = []
    optimum = True
    for n in l:
        x = (100 * float(n) / N)
        x -= int(x)
        if x < 0.5:
            x = 0.5 - x
            optimum = False
        d.append(x)
    return d, optimum

def solve():
    N, L = map(int, raw_input().split())
    l = map(int, raw_input().split())

    delta = (100. / N)
    delta -= int(delta)
    remaining = N - sum(l)

    percent(N, l)
    while remaining:
        if delta >= 0.5:
            l.append(1)
        else:
            d, optimum = deltas(N, l)
            if not optimum:
                min_index, _ = min(enumerate(d), key=operator.itemgetter(1))
                l[min_index] += 1
            else:
                l.append(1)
        percent(N, l)
        remaining -= 1
    return percent(N, l)


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
