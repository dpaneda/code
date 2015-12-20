#!/usr/bin/python2

import sys

k = 0
ps = 0
pr = 0
pu = 0
pw = 0
pd = 0
pl = 0
cache = {}
hit = 0
miss = 0


def normalize(pi):
    if pi > 1000:
        return 1000
    elif pi < 0:
        return 0
    return round(pi, 9)


def match_win(pi, win, lost):
    global k, ps, pr, pu, pw, pd, pl, cache, hit, miss
    if (pi, win, lost) in cache:
        hit += 1
        return cache[(pi, win, lost)]
    miss += 1
    pi = normalize(pi)

    if win == k:
        return 1000

    if lost == k:
        return 0

    # conditionals of the remaing match if wins or loses
    w = pw * match_win(pi + pu, win + 1, lost) + ((1000 - pw) * match_win(pi, win + 1, lost))
    w /= 1000 * 1000
    l = pl * match_win(pi - pd, win, lost + 1) + ((1000 - pl) * match_win(pi, win, lost + 1))
    l /= 1000 * 1000

    #print w
    #print l
    #print pi * ps * w
    #print pi * (1 - ps) * l
    #print (1 - pi) * pr * w
    #print (1 - pi) * (1 - pr) * l

    result = (pi * ps * w) + (pi * (1000 - ps) * l) + ((1000 - pi) * pr * w) + ((1000 - pi) * (1000 - pr) * l)
    result /= 1000 ** 4
    cache[(pi, win, lost)] = result
    return result


def Solve():
    global k, ps, pr, pu, pw, pd, pl, cache, hit, miss
    hit = miss = 0
    k, ps, pr, pi, pu, pw, pd, pl = map(float, sys.stdin.readline().strip().split())
    ps = int(1000 * ps)
    pr = int(1000 * pr)
    pi = int(1000 * pi)
    pu = int(1000 * pu)
    pw = int(1000 * pw)
    pd = int(1000 * pd)
    pl = int(1000 * pl)
    cache = {}
    result = match_win(pi, 0, 0)
    print (1.0 * hit) / (hit + miss)
    return "%.6f" % (result / 1000.0)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
