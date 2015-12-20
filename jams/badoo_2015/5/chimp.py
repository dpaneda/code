#!/usr/bin/python2

import sys

raw_input()

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

sys.setrecursionlimit(15000)

@memoize
def f(n):
    if n <= 2:
        return n
    elif n == 3:
        return 5
    return f(n-1) + 2 * f(n-2) + 1 

for line in sys.stdin:
    n = int(line)
    print f(n)
    continue
