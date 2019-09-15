#!/usr/bin/python2

import sys

def solve():
    a, b = map(int, raw_input().split())
    n = input()
    while True:
        k = (b - a + 1) / 2
        print(a + k)
        sys.stdout.flush()
        n -= 1
        s = raw_input()
        if s == 'CORRECT':
            return True
        elif s == 'TOO_SMALL':
            a += k
        elif s == 'TOO_BIG':
            b -= k - 1
        else:
            return False
        if n <= 0:
            return False

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    if not solve():
        sys.stderr.write("Something go wrong, exit")
        sys.exit(1)
