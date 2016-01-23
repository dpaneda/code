#!/usr/bin/python2

import sys

a = 0
b = 0
palindromes = {}


def in_range(n):
    return n >= a and n <= b


def Solve():
    global a, b
    a, b = map(int, sys.stdin.readline().split())

    return len(filter(in_range, palindromes))


def dale(n):
    n = int(n)
    palindromes[n * n] = n


def palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


for n in range(1, 1000):
    if palindrome(n) and palindrome(n * n):
        palindromes[n * n] = n


for digits in range(4, 50):
    binlen = int((digits - 2) / 2)
    for p in range(0, 2 ** binlen):
        p1 = bin(p)[2:]
        if p1.count('1') > 3:
            continue
        if len(p1) < binlen:
            p1 = '0' * (binlen - len(p1)) + p1
        p2 = p1[::-1]
        if digits % 2:
            dale('1' + p1 + '0' + p2 + '1')
            dale('1' + p1 + '1' + p2 + '1')
        else:
            dale('1' + p1 + p2 + '1')

    n = '2' + '0' * (digits - 2) + '2'
    dale(n)

    if digits % 2:
        ceros = int((digits - 3) / 2)
        n = '2' + '0' * ceros + '1' + '0' * ceros + '2'
        dale(n)
        n = '1' + '0' * ceros + '2' + '0' * ceros + '1'
        dale(n)
        for p in range(0, ceros):
            p1 = '0' * p + '1' + '0' * (ceros - p - 1)
            p2 = p1[::-1]
            n = '1' + p1 + '2' + p2 + '1'
            dale(n)

#for n in palindromes:
#    print(palindromes[n], n)

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
