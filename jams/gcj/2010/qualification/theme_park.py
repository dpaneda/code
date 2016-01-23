#!/usr/bin/python
import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
    R, k, s = map(int, sys.stdin.readline().split())
    groups = map(int, sys.stdin.readline().split())

    next, money, ride = 0, 0, 0
    jump = False

    while ride < R:        
        if next == 0 and money > 0 and not jump:
           ride = R - (R % ride)
            money *= ride
            jump = True
            continue
        ride += 1
        free = k
        first = None
        while free >= groups[next] and first != next:
            if first is None:
                first = next
            free -= groups[next]
            money += groups[next]
            next = (next + 1) % len(groups)
    
    print "Case #%d: %d" % (i, money)
