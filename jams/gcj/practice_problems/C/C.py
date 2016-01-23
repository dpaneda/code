#!/usr/bin/python2

import sys


def Solve():
    board = []
    for i in range(0, 4):
        board.append(sys.stdin.readline().strip())
    sys.stdin.readline().strip()


    return 'Draw'


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
