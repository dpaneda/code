#! /usr/bin/env python

import sys


def score(a, b):
    win =  { 'A': 'Y', 'B': 'Z', 'C': 'X' }
    draw = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
    lose = { 'A': 'Z', 'B': 'X', 'C': 'Y' }

    shape_score = { 'X': 1, 'Y': 2, 'Z': 3 }

    sc = 0

    if b == 'X':
        b = lose[a]
    elif b == 'Y':
        b = draw[a]
        sc += 3
    else:
        b = win[a]
        sc += 6
    
    sc += shape_score[b]

    return sc

total_score = 0
for line in sys.stdin:
    a, b = line.split()
    total_score += score(a, b)
print(total_score)
