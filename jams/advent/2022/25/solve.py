#! /usr/bin/env python
import sys
import math

def snafu_decode(c):
    if c == '-':
        return -1
    if c == '=':
        return -2
    return int(c)

def snafu_encode(n):
    if n == -1:
        return '-'
    if n == -2:
        return '='
    return str(n)

def snafu_to_decimal(s):
    n = 0
    v = 1
    l = list(map(snafu_decode, s))

    while l:
        n += v * l.pop()
        v *= 5
    return n


def decimal_to_snafu(n):
    def first_power(n):
        power = int(math.log(n, 5))
        for p in power, power+1:
            for symbol in 1, 2:
                value = symbol * 5**p
                if value >= n:
                    return p, symbol

    def power_symbol(n, power):
        if n < 0:
            neg = -1
            n = abs(n)
        else:
            neg = 1
        best_value = n
        best = 0
        for symbol in 0, 1, 2:
                value = n - symbol * 5**power
                if abs(value) < abs(best_value):
                    best_value = value
                    best = neg * symbol
        return best

    power, symbol = first_power(n)
    powers = {power: symbol}
    s = f"{symbol}"
    n -= symbol * 5**power
    for power in range(power - 1, -1, -1):
        symbol = power_symbol(n, power)
        powers[power] = s
        n -= symbol * 5**power
        s += snafu_encode(symbol)
    return s

n = 0
for line in sys.stdin:
    n += snafu_to_decimal(line.strip())
print(n)
print(decimal_to_snafu(n))
