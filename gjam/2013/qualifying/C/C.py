#!/usr/bin/python2

import sys


def palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def Solve():
    a, b = map(int, sys.stdin.readline().split())

    with open("fairs") as f:
        content = map(int, f.readlines())

    print content
    return

    n = 0
    count = 0
    while True:
        n += 1
        p = n * n
        if p < a:
            continue

        if p > b:
            break

        if palindrome(n) and palindrome(p):
            count += 1

    return count


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
