#!/usr/bin/python

import sys
import heapq


def read_integers():
    return list(map(int, input().split()))

def Solve():
    L, N, M, D = read_integers()
    W = read_integers()
    w = [[x, x] for x in W]
    heapq.heapify(w)

    wash_times = []

    # Washing simulation
    washer = heapq.heappop(w)
    for _ in range(0, L):
        wash_times.append(washer[0])
        washer[0] += washer[1]
        washer = heapq.heappushpop(w, washer)

    if M >= L:
        # More dryers than loads, time is just drying the last load
        return wash_times[-1] + D

    # Drying simulation
    m = [0 for _ in range(0, M)]
    dry_slot = heapq.heappop(m)
    for t in wash_times:
        last_dry = max(t + D, dry_slot + D)
        dry_slot = heapq.heappushpop(m, last_dry)

    return last_dry
   

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print("Case #%d: %s " % (case, Solve()))
