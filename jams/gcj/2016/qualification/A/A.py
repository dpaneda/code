#!/usr/bin/python3

import sys

def digits(n):
    d = set()
    while n:
        d.add(n % 10)
        n //= 10
    return d

def solve():
    n = int(input())

    if n == 0:
        return 'INSOMNIA'

    d = set()
    i = 0
    while len(d) != 10:
        i += 1
        d |= digits(n * i)
    return n * i

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
