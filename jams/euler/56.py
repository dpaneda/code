#!/usr/bin/env python3

def sum_digits(n):
  return sum(map(int, str(n)))

m = 0

for a in range(1, 100):
  for b in range(1, 100):
    if sum_digits(a**b) > m:
      m = sum_digits(a**b)

print(m)
