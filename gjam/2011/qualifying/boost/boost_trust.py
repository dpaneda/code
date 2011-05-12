#!/usr/bin/python

import sys

def distance(a, b):
    if a > b:
        return a - b
    return b - a

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    orders = sys.stdin.readline().split()
    pos = {}
    goto = {}
    pos['O'] = 1
    pos['B'] = 1
    goto['O'] = []
    goto['B'] = []
    i = 1
    while i < len(orders):
       robot = orders[i]
       button = int(orders[i+1])
       goto[robot].append(button)
       i += 2

    seconds = 0

    i = 1
    while i < len(orders):
        advance = False
        robot = orders[i]
        button = int(orders[i+1])

        if pos[robot] == button:
            advance = True
            i += 2

        for r in 'O' 'B':
            if len(goto[r]):
                if pos[r] < goto[r][0]:
                    pos[r] += 1
                elif pos[r] > goto[r][0]:
                    pos[r] -= 1
        
        seconds += 1

        if advance:
            goto[robot].pop(0)

    print "Case #%d: %s" % (case, seconds)
