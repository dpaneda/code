#!/usr/bin/python

import sys
import heapq


def read_integers():
    return list(map(int, input().split()))

def Solve():
    N , A, B = read_integers()
    C = read_integers()
    Y = sum(C)
    steps = len(C)

    # Search initial step
    n = A % Y
    s = 0

    if C[s] > B:
        a, b = A, B
        l = B - A
        average = (a + b) / 2
        return average

    while True:
        if n >= C[s]:
            n -= C[s]
            s = (s + 1) % steps
        else:
            break

    rest = C[s] - n
    a, b = n, C[s]
    average = (a + b) / 2
    l = rest
    total = average * l

    n = A + rest
    while n + C[s] < B:
        s = (s + 1) % steps
        a, b = 0, C[s]
        average = (a + b) / 2
        l = C[s]
        total += average * l
        n += C[s]

    a, b = 0, (B - n)
    average = (a + b) / 2
    l = B - n
    total += average * l
    return total / (B - A)
   

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, Solve()))
