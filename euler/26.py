#!/usr/bin/python

from decimal import Decimal, getcontext


def has_cycle(s, n):
  for i in range(0, 10):
    a = i*n
    b = a + n
    c = b + n
    if s[a:b] != s[b:c]:
      return False
    return True

getcontext().prec = 1000

cycle_max = 0

for i in range(1, 10):
  ns = str(Decimal(1) / Decimal(i))[2:]
  if len(ns) <1000:
    continue
  cycle_len = 100
  while not has_cycle(ns, cycle_len):
    cycle_len -= 1
  if cycle_len > cycle_max:
    cycle_max = cycle_len

print(cycle_len)
