#!/usr/bin/env python3

n = 12252240

while True:
  for i in range(2, 21):
    if n % i:
      break
  if i != 20:
    n += 1
    continue
  else:
    break

print(n)
