#!/usr/bin/python2

import sys
import math

def solve():
    D, P = raw_input().split()
    D = int(D)
    beam = 1
    damage = 0
    hack_values = []
    for c in P:
        if c == 'C':
            hack_values.append(0)
            beam *= 2
        else:
            damage += beam
            if hack_values:
                hack_values[-1] += 1

    hacks = 0
    overload = damage - D

    while overload > 0 and hack_values:
        hack_value = 2**(len(hack_values) - 1)
        n = hack_values.pop()
        if hack_value * n < overload:
            hacks += n
            if hack_values:
                hack_values[-1] += n
            overload -= hack_value * n
        else:
            hacks += (overload + hack_value - 1) / hack_value
            overload = 0 

    if overload <= 0:
        return hacks
    else:
        return "IMPOSSIBLE"


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
