#!/usr/bin/env python3

from math import factorial

def combinations(n, r):
  return factorial(n) / (factorial(r) * factorial(n-r)) 

exceeds = 0

for n in range(1, 101):
  for r in range(1, n):
    if combinations(n, r) > 1000000:
      exceeds += 1

print(exceeds)
