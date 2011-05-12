#!/usr/bin/python

import sys

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    sys.stdin.readline() # skip
    l = map(int, sys.stdin.readline().split())
    l.insert(0, 0) # Now l[i] should be i for every position
    hits = 0
    ordered = False
    while not ordered:
        ordered = True
        bad = None
        for i in range(0, len(l)):
            if l[i] == i:
                continue
            #print i, l
            ordered = False
            j = l[i]
            # Permutation possible ?
            if l[j] == i:
                hits += 2
                l[i] = i
                l[j] = j
            elif bad and i == l[bad]:
                hits += 2
                tmp = l[i]
                l[i] = l[bad]
                l[bad] = tmp
                bad = None
            elif not bad:
                bad = i

    print "Case #%d: %d" % (case, hits)
