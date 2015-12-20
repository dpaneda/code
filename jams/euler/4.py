#!/usr/bin/env python3

def is_palindrome(n):
  nl = list(str(n))
  nl.reverse()
  return nl == list(str(n))

max = 0
for x in range(1, 1000):
  for y in range(1, 1000):
    if is_palindrome(x * y) and max < x * y:
      max = x * y

print(max)
