#!/usr/bin/env python3

n = 2**1000

sum = 0
for digit in str(n):
  sum += int(digit)

print(sum)
