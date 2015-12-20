#!/usr/bin/env python3

def hexagonal(n):
  return int (n * (2*n - 1))

def pentagonal(n):
  return int (n * ((3 * n) - 1) / 2)

def triangle(n):
  return int (n * (n + 1) / 2)

p = set()
t = set()
h = set()

for n in range(1, 200000):
  p.add(pentagonal(n))
  t.add(triangle(n))
  h.add(hexagonal(n))

all_in = p.intersection(t).intersection(h)

print(all_in)
