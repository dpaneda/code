#!/usr/bin/python2

import os
import sys
import random
import itertools

def fake_get(a, b):
    return random.choice("ABCDE")

def get(a, b):
    n = (5 * a) + b
    print(n + 1)
    sys.stdout.flush()
    return raw_input().strip()

def solve():
    rangers = [''.join(p) for p in itertools.permutations('ABCDE')]
    hrangers = []
    for i in xrange(119):
        s = ''
        for j in xrange(4):
            if i == 118 and j == 3:
                continue
            s += get(i, j)
        hrangers.append(s)

    for perm in itertools.permutations('ABCDE', 4):
        perm = ''.join(perm)
        if hrangers.count(perm):
            rangers = list(filter(lambda r: not r.startswith(perm), rangers))

    print(rangers[0])

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
cases, F = map(int, raw_input().split())
for case in xrange(cases):
    solve()
