#!/usr/bin/python

import sys

def Solve():
    input()
    problems = list(map(int, input().split()))
    added = 0
    i = -1
    while problems:
        i += 1
        if i % 4 == 0:
            current = problems.pop(0)
        else:
            next = problems[0]
            if next <= current or next > current + 10:
                added += 1
                current += 10
            else:
                current = problems.pop(0)
    added += 3 - (i % 4)
    return added

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, Solve()))
