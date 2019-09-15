#!/usr/bin/python3

import sys
import operator

def solve():
    s = reversed(input())
    s = list(map(lambda c: True if (c == '+') else False, s))
    flips = 0
    while False in s:
        index = s.index(False)
        s = s[:index] + list(map(operator.not_, s[index:]))
        flips += 1
    return flips

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
