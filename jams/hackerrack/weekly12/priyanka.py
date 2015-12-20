#!/usr/bin/python2

import sys
import math

num = int(sys.stdin.readline())

ws = map(int, sys.stdin.readline().split())
ws.sort()

actual = -5
units = 0

for w in ws:
    if w > actual + 4:
        units += 1
        actual = w

print(units)

