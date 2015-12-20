#!/usr/bin/env python3

def is_palindrome(n):
  nl = list(n)
  nl.reverse()
  return nl == list(n)

s = 0
for n in range(1, 1000000):
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
      s += n

print(s)
