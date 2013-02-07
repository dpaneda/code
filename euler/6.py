#!/usr/bin/env python3

s = 0
sq = 0

for i in range(1, 101):
  print(i)
  s += i
  sq += i*i

print(s)
print(sq)

print(s*s - sq)
