#!/usr/bin/env python3

str_n = ""
i = 0

while len(str_n) < 1000001:
  str_n += str(i)
  i += 1

def d(n):
  return int(str_n[n])

print(d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000))
