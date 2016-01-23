#!/usr/bin/python2

import sys


def search_consecutive(name, n):
    consecutive = set()
    vowels = 'aeiou'
    ini = 0
    end = 0
    for i in xrange(0, len(name)):
        if name[i] in vowels:
            ini = end = i + 1
        elif end - ini >= n - 1:
            if (ini, end-1) in consecutive:
                consecutive.remove((ini, end-1))
            consecutive.add((ini, end))
            #ini += 1
            end += 1
        else:
            end += 1
    print consecutive
    return consecutive


def Solve():
    (name, n) = sys.stdin.readline().strip().split()
    n = int(n)
    consecutive = search_consecutive(name, n)
    substrings = set()
    for c in consecutive:
        for i in xrange(0, 1 + c[0]):
            for j in xrange(c[1], len(name)):
                substrings.add((i, j))
    return len(substrings)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
