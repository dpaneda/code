#!/usr/bin/env python3

MAX = 100

terms = set()

for a in range(2, MAX + 1):
  for b in range(2, MAX + 1):
    terms.add(a**b)

print(len(terms))
