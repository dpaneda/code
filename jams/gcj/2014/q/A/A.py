#!/usr/bin/python2

import sys


def solve():
    first_row = int(sys.stdin.readline())
    for i in xrange(1, 5):
        if i == first_row:
            candidates_row = set(map(int, sys.stdin.readline().strip().split()))
        else:
            sys.stdin.readline()
    second_row = int(sys.stdin.readline())
    for i in xrange(1, 5):
        if i == second_row:
            row = set(map(int, sys.stdin.readline().strip().split()))
        else:
            sys.stdin.readline()

    carts = candidates_row & row

    if not carts:
        return 'Volunteer cheated!'
    elif len(carts) > 1:
        return 'Bad magician!'
    else:
        return str(list(carts)[0])

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #%d: %s " % (case, solve())
