#!/usr/bin/env python3

from math import factorial

n = factorial(100)

sum = 0
for digit in str(n):
  sum += int(digit)

print(sum)
