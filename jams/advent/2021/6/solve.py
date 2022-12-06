#!/usr/bin/env python
from functools import cache

@cache
def simulate(fish, days):
    if days == 0:
        return 1
    else:
        days -= 1
        if fish > 0:
            return simulate(fish - 1, days)
        else:
            return simulate(8, days) + simulate(6, days)

fishes = map(int, input().split(','))

total = sum(map(lambda f : simulate(f, 256), fishes))
print(total)
