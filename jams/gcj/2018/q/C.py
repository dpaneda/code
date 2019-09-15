#!/usr/bin/python2

import sys
import math

def solve():
    a = input()
    n = int(math.ceil(math.sqrt(a)))
    prepared = set()

    def ready(a, b):
        for i in xrange(a - 1, a + 2):
            for j in xrange(b - 1, b + 2):
                if (i, j) not in prepared:
                    return False
        return True

    def prepare(i, j):
        print i + 10, j + 10
        sys.stdout.flush()

    def mark(i, j):
        prepared.add((i - 10, j - 10))

    if n < 3:
        n = 3

    for i in xrange(0, n + 1, 3):
        for j in xrange(0, n + 1, 3):
            while not ready(i, j):
                prepare(i, j)
                s = raw_input()
                a, b = map(int, s.split())
                if a == -1:
                    sys.stderr.write("ERROR\n")
                    return
                if a + b == 0:
                    return
                mark(a, b)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    solve()
