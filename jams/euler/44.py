#!/usr/bin/env python3

from itertools import combinations

def abs(n):
  if n < 0:
    n = -n
  return n

def pentagonal(n):
  return int (n * ((3 * n) - 1) / 2)

pentagonals = set()

for n in range(1, 5000):
  pentagonals.add(pentagonal(n))

best = (99999999999, 0, 0)

for comb in combinations(pentagonals, 2):
  a = comb[0] + comb[1]
  b = abs(comb[0] - comb[1])

  if a in pentagonals and b in pentagonals:
    if best[0] > b:
      best = (b, comb[0], comb[1])
    
print(best)
