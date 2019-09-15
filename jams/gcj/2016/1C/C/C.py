#!/usr/bin/python2

import sys
from collections import Counter

def find_best(jp, js, ps, last):
    best = None
    best_sum = 999999999999999
    for jpi, jpv in jp.iteritems():
        for jsi, jsv in js.iteritems():
            for psi, psv in ps.iteritems():
                s = jpv + jsv + psv
                t = jpi, jsi, psi
                if s < best_sum and t != last:
                    best_sum = s
                    best = t
    return best

def check_ok(jp, js, ps, k):
    for v in jp.itervalues():
        if v > k:
            return False
    for v in js.itervalues():
        if v > k:
            return False
    for v in ps.itervalues():
        if v > k:
            return False
    return True
 

def solve():
    J, P, S, K = map(int, raw_input().split())
    jp = {}
    js = {}
    ps = {}

    for i in xrange(J):
        for j in xrange(P):
            jp[(i, j)] = 0

    for i in xrange(J):
        for j in xrange(S):
            js[(i, j)] = 0

    for i in xrange(P):
        for j in xrange(S):
            ps[(i, j)] = 0

    last = None
    outfits = []
    while True:
        t = find_best(jp, js, ps, last)
        if not t: 
            break
        a, b, c = t
#        print t
        jp[a] += 1
        js[b] += 1
        ps[c] += 1
#        print jp
        if check_ok(jp, js, ps, K):
            outfits.append(t)
            last = t
        else:
            break

    print len(outfits)
    for o in outfits:
        a, b, c = o
        print a[0] + 1, a[1] + 1, c[1] + 1

    return " "

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}:".format(case),
    solve()
