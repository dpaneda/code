#!/usr/bin/python

import sys


def read_integers():
    return list(map(int, input().split()))

def Solve():
    N = input()
    A = input()
    B = input()

    middle = (len(A) + 1) // 2
    middle -= 1

    a_paints = 0
    lastpaint = None
    for i in range(middle, -1, -1):
        if A[i] != B[i] and B[i] != lastpaint:
            lastpaint = B[i]
            a_paints += 1

    b_paints = 0
    lastpaint = None
    for i in range(middle + 1, len(A)):
        if A[i] != B[i] and B[i] != lastpaint:
            lastpaint = B[i]
            b_paints += 1

    return max(a_paints, b_paints)
    
num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, Solve()))
