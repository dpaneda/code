#!/usr/bin/python2

import sys
import random

def solve():
    N, L = map(int, raw_input().split())
    letters = []
    words = set()
    for _ in xrange(L):
        letters.append(set())
    for _ in xrange(N):
        word = raw_input()
        words.add(word)
        for i in xrange(len(word)):
            letters[i].add(word[i])

    letters = map(list, letters)
    n = len(letters[0])
    for i in xrange(1, L):
        n *= len(letters[i])
    if (n - N) == 0:
        return '-'

    while True:
        s = ''
        for i in xrange(L):
            s += random.choice(letters[i])
        if s not in words:
            return s

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
