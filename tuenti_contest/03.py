#!/usr/bin/python

import sys
from math import sqrt


def is_prime(n):
    if n == 2: 
        return True
    if n < 2 or n % 2 == 0: 
        return False
    return not any(n % i == 0 for i in range(3, int(sqrt(n)) + 1, 2))

def is_emirp(number):
    reversed_number = int("".join(reversed(str(number))))
    if number == reversed_number:
        return False
    else:
        return is_prime(number) and is_prime(reversed_number)

for line in sys.stdin:
    n = int(line)
    sum = 0
    for i in xrange(1, n):
        if is_emirp(i):
            sum += i
    print sum
