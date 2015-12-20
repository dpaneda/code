#!/usr/bin/env python3

import math

def is_curious(n):
  s = 0

  for digit in str(n):
    s += math.factorial((int(digit)))

  return s == n


s = 0
for n in range(10, 1000000):
  if is_curious(n):
    print(n)
    s += n

print(s)
