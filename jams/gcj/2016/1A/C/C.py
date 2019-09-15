#!/usr/bin/python3

import sys

def search(bff, n):
    s = [n]
    cont = True
    while cont:
        cont = False
        last = s[-1]
        print(s, last)
        if bff[last] not in s:
            cont = True
            s.append(bff[last])

    if bff[s[-1]] != s[0]:
        return 0
    print(n, s)
    return len(s)

def solve():
    n = int(input())

    bff = [0] + list(map(int, input().split()))
    print(bff)
    m = 0
    for i in range(1, len(bff)):
        m = max(m , search(bff, i))
    return m


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
