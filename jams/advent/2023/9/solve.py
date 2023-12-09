#! /usr/bin/env python
import sys

def get_diff(l):
    k = []
    for i in range(len(l) - 1):
        a, b = l[i:i+2]
        k.append(b - a)
    return k

def extrapolate(l):
    steps = []
    while any(l):
        steps.insert(0, l)
        l = get_diff(l)
    first, last = 0, 0
    for l in steps:
        first, last = l[0] - first, l[-1] + last
        l = [first] + l + [last]
    return first, last

first, last = 0, 0
for line in sys.stdin:
    l = list(map(int, line.split()))
    a, b = extrapolate(l)
    first, last = first + a, last + b
print(first, last)
