#!/usr/bin/python

from decimal import Decimal, getcontext


def has_cycle(s, n):
    for i in range(0, 10):
        a = i * n
        b = a + n
        c = b + n
        if s[a:b] != s[b:c]:
            return False
    return True

getcontext().prec = 30000

cycle_max = 0

for i in range(1, 1000):
    ns = str(Decimal(1) / Decimal(i))[2:]
    if len(ns) < 1000:
        continue
    for cycle_len in range(1, 30000):
        if has_cycle(ns, cycle_len):
            if cycle_len > cycle_max:
                print (i, cycle_len)
                cycle_max = cycle_len
            break
