#!/usr/bin/env python3


def ways(n):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    ncoins = [0,   0,  0,  0,  0, 0, 0, 0]

    if n < 0:
        return 0
    elif n == 0:
        return 1

    w = 0

    for coin in coins:
        w += ways(n - coin)
        print(n, coin, w)

    return w

print(ways(5))
#print(ways(200))
