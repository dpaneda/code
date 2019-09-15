#!/usr/bin/python2

import sys

def start(a):
    return a[0]

def end(a):
    return a[1]

def solve():
    C, J = map(int, raw_input().split())
    c = []
    j = []

    for i in xrange(0, C):
        a, b = map(int, raw_input().split())
        c.append((a, b))
    for i in xrange(0, J):
        a, b = map(int, raw_input().split())
        j.append((a, b))

    c.sort()
    j.sort()

    if C < 2 and J < 2:
        return "2"

    if C > 1:
        l = c
    elif J > 1:
        l = j

    if end(l[1]) - start(l[0]) <= 720:
        return "2"

    if (1440 + end(l[0]) - start(l[1])) <= 720:
        return "2"
    
    return "4"

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
