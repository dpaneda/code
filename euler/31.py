#!/usr/bin/env python3


def ways(n):
  coins =  [200, 100, 50, 20, 10, 5, 2, 1]
  ncoins = [  0,   0,  0,  0,  0, 0, 0, 0]

  if n == 1:
    return 1
  elif n == 0:
    return 999999

  w = 1

  for coin in coins:
    while n > 0 and coin <= n:
      w += ways(coin)
      n -= coin
      if n == 0:
        return w

print(ways(2))
#print(ways(200))
