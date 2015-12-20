#!/usr/bin/python

import time
import numpy
import sys
from math import sqrt, log
 
memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
            memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fibonacci2(n):
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return int(0.5 + phi**n/root5)

phi = (1 + 5**0.5) / 2

def fibonacci3(f):
    if f < 2:
        return f
    return int(round(log(f * 5**0.5) / log(phi)))

sys.setrecursionlimit(100000)

i = 0
while len(str(fib(i))) < 1000:
  i += 1

print(i)
