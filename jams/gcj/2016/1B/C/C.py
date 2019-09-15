#!/usr/bin/python3

import sys
from collections import Counter

def solve():
    n = int(input())
    soldiers = []
    for _ in range(1, 2*n):
        l = list(map(int,input().split()))
        soldiers += l
    soldiers.sort()
    choosen = []
    s = Counter(soldiers)
    for k in s:
        if s[k] % 2:
            choosen.append(k)
    choosen.sort()
    choosen = map(str, choosen)
    return " ".join(choosen)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
