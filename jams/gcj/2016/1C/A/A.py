#!/usr/bin/python2

import sys
import operator

def print_leave(a, b=None):
    s = chr(a + ord('A'))
    if b is not None:
        s += chr(b + ord('A'))
    s += " "
    return s

def check_ok(p, parties):
    for n in p.itervalues():
        if n > parties / 2:
            return False
    return True

def find_max(p):
    sorted_p = sorted(p.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_p[0][0]

def solve():
    s = ''
    raw_input()
    parties = 0
    p = {}
    i = 0
    for n in map(int, raw_input().split()):
        p[i] = n
        parties += n
        i += 1

    while parties > 0:
        a = find_max(p)
    
        p[a] -= 1
        parties -= 1
        if check_ok(p, parties):
            s += print_leave(a)
        else:
            b = find_max(p)
            p[b] -= 1
            parties -= 1
            s += print_leave(a, b)
       
    return s

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
