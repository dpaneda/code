#!/usr/bin/python2

import sys
import operator


def valid(i, j, s):
    M = s[i][0] + s[i][1]
    N = None

    print M, N

    m_valid = True
    n_valid = True

    for d, a, b in s[i : j + 1]:
        if M != d + a:
            m_valid = False
            if not N:
                N = d - b
        if N != d - b:
            n_valid = False

    return m_valid or n_valid

def solve():
    S = input()
    s = []
    for _ in range(S):
        s.append(map(int, raw_input().split()))

    max_size = 0
    valid_sets = 0

    print valid(0, S - 1, s)
    return 0, 0

    for i in xrange(0, S):
        for j in xrange(i, S):
            if not valid(i, j, s):
                break
            size = j - i + 1
            if size > max_size:
                max_size = size
                valid_sets = 1
            elif size == max_size:
                valid_sets +=1

    return max_size, valid_sets


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    a, b = solve()
    print("Case #{0}: {1} {2}".format(case, a, b))
