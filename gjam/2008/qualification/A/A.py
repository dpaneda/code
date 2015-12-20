#!/usr/bin/python2

import sys


def count_switchs(webs, search):
    changes = -1
    index = 0
    if not search:
        return 0
    while index < len(search):
        m = 0
        for web in webs:
            try:
                i = search.index(web, index)
                if i > m:
                    m = i
            except ValueError:
                return changes + 1
        index = m
        changes += 1
    return changes


def Solve():
    nwebs = int(sys.stdin.readline())
    webs = {}
    for i in xrange(0, nwebs):
        webs[sys.stdin.readline()] = 1
    nsearch = int(sys.stdin.readline())
    search = []
    for i in xrange(0, nsearch):
        search.append(sys.stdin.readline())

    return count_switchs(webs, search)


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
