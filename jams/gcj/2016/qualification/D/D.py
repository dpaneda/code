#!/usr/bin/python3

import sys

def solve():
    K, C, S = map(int, sys.stdin.readline().split())
    s = map(str, range(1, S + 1))
    return " ".join(s)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
