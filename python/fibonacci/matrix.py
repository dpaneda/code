#!/usr/bin/python

import time
import numpy
import sys
from math import sqrt, log
 
fibonacci_matrix = numpy.matrix([[1,1],[1,0]])


memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
            memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fibonacci(n):
    return (fibonacci_matrix**(n-1)) [0,0]

def fibonacci2(n):
    root5 = sqrt(5)
    phi = 0.5 + root5/2
    return int(0.5 + phi**n/root5)


phi = (1 + 5**0.5) / 2

def fibonacci3(f):
    if f < 2:
        return f
    return int(round(log(f * 5**0.5) / log(phi)))

start = time.clock()
i = int(sys.argv[1])
print fib(i)
print fibonacci(i)
print fibonacci2(i)
print fibonacci3(i)
end = time.clock()



print "Time elapsed = ", end - start, "seconds"
