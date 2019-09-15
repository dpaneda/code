#!/usr/bin/python3
import math

def solve():
    N, K, V = list(map(int, input().split()))
    l = []
    for i in range(N):
        l.append(input())

    first = ((V - 1) * K) % N
    visited = set()
    for i in range(first, first + K):
        if i < N - 1:
            visited.add(l[i])
        else:
            visited.add(l[i - N])

    result = []
    for i in range(N):
        if l[i] in visited:
            result.append(l[i])
    return " ".join(result)

num = int(input())

for case in range(1, num + 1):
    print("Case #%d: %s" % (case, solve()))
