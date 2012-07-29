#!/usr/bin/env python

total = 2
a, b = 1, 2

while True:
  a, b = b, a + b
  if b > 4000000:
    break

  print(b)
  if b % 2:
    total += b
    
print(total)
