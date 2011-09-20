#!/usr/bin/python

import sys
import itertools

def solve_with(ncows, maxweight, weight, prod):
    max_milk = 0
    for comb in itertools.combinations(range(len(weight)), ncows):
        milk, w = 0, 0
        for i in comb:
            milk += prod[i]
            w += weight[i]
        if w < maxweight and milk > max_milk:
            max_milk = milk
    return max_milk

def solve(maxweight, weight, prod):
    cows = len(weight)
    for i in xrange(cows, 1, -1):
        s = solve_with(i, maxweight, weight, prod)
        if s:
            return s

for line in sys.stdin:
    l = line.split()
    maxweight = int(l[1])
    weight = map(int, l[2].split(','))
    prod = map(int, l[3].split(','))
    print solve(maxweight, weight, prod)
