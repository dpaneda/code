#!/usr/bin/python

import sys

def patrick_add(a, b):
    return (a | b) - (a & b)

def patrick_add_list(l):
    sum = 0
    for i in l:
        sum = patrick_add(sum, i)
    return sum

def list_sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    sys.stdin.readline() # skip
    candys = map(int, sys.stdin.readline().split())
    candys.sort()
    if patrick_add_list(candys) != 0:
        print "Case #%d: NO" % case
    else:
        candys.pop(0)
        print "Case #%d: %d" % (case, list_sum(candys))
