#!/usr/bin/python

import sys

cases, a, b = map(int, input().split())

def solve():
    for x in range(-5, 5):
        for y in range(-5, 5):
            print("{} {}".format(x, y), flush=True)
            s = input()
            if s == 'CENTER':
                return

for case in range(cases):
    solve()
