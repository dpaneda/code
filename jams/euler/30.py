#!/usr/bin/env python3

POWER = 5

terms = []

for i in range(10, 1000000):
  s = 0
  for digit in str(i):
    s += (int(digit)**POWER)
  if (s == i):
    terms.append(s)

s = 0
for term in terms:
  s += term
  print(term)

print(s)
