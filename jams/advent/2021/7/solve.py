#!/usr/bin/env python

l = list(map(int, input().split(',')))

def fuel(l, pos):
    total = 0
    for n in l:
        d = abs(n - pos)
        total +=  d * (d + 1) // 2
    return total

a, b = min(l), max(l)
best_fuel = min(range(a, b), key=lambda p : fuel(l, p))
print(best_fuel)
