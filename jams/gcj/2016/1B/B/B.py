#!/usr/bin/python3

import sys

def ltoi(l):
    n = 0
    for d in l:
        n = 10 * n + d
    return n

def great_test(C, J, i):
    c = C[i:]
    j = J[i:]
    c[i] = 0
    j[i] = 0
    c = [9 if n is None else n for n in c]
    j = [0 if n is None else n for n in j]
    a = ltoi(c)
    b = ltoi(j)
    d = abs(a - b)

    c = C[i:]
    j = J[i:]
    c[i] = 1
    j[i] = 0
    c = [0 if n is None else n for n in c]
    j = [9 if n is None else n for n in j]
    a = ltoi(c)
    b = ltoi(j)
    d2 = abs(a - b)
    #print(d, d2)

    return d2 < d

def greater(C, J):
    n = len(C)
    for i in range(0, n):
        if C[i] is None and J[i] is None:
            if i > n - 2:
                continue
        if C[i] is None or J[i] is None:
            continue
        if C[i] == J[i]:
            continue
        if C[i] > J[i]:
            return 'C', i
        else:
            return 'J', i
    return None, 999999

def pad(C, J):
    n = len(C)
    for i in range(0, n):
        if C[i] is None and J[i] is None:
            if i <= n - 2 and C[i+1] is not None and J[i+1] is not None:
                if great_test(C, J, i):
                    C[i] = 1
                    J[i] = 0
                elif great_test(J, C, i):
                    C[i] = 0
                    J[i] = 1
            if C[i] is None:
                C[i] = 0
                J[i] = 0
        else:
            return

def tie_on_next(C, J, j):
    n = len(C)
    for i in range(j + 1, n):
        if C[i] is None and J[i] is None:
            continue
        if C[i] is None or J[i] is None:
            return False
        tie = (C[i] - J[i]) % 5
        return tie == 0
    return False

def fill(C, J):
    n = len(C)
    g, where = greater(C, J)
#    print(C, J, g, where)
#    print(g)
#    print(C, J)
    for i in range(0, n):
        if C[i] is None and J[i] is None:
            C[i] = 9 if g == 'J' else 0
            J[i] = 9 if g == 'C' else 0
        elif C[i] is not None and J[i] is not None:
            continue
        elif C[i] is None and J[i] is not None:
            if g == 'J' and i > where:
                C[i] = 9
            elif tie_on_next(C, J, i) and J[i] > 0:
                C[i] = J[i] - 1
            elif i < where:
                C[i] = J[i]
            else:
                C[i] = 0
        elif J[i] is None and C[i] is not None:
            if g == 'C' and i > where:
                J[i] = 9
            elif tie_on_next(C, J, i) and C[i] > 0:
                J[i] = C[i] - 1
            elif i < where:
                J[i] = C[i]
            else:
                J[i] = 0
        elif C[i] is None:
            C[i] = 9 if g == 'C' else 0
        elif J[i] is None:
            J[i] = 9 if g == 'J' else 0


def solve():
    C, J = input().split()
    C = [None if c == '?' else int(c) for c in C]
    J = [None if c == '?' else int(c) for c in J]
    pad(C, J)
    fill(C, J)
    C = list(map(str, C))
    J = list(map(str, J))
    return "{} {}".format(''.join(C), ''.join(J))


num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
