#! /usr/bin/env python

import sys


def score(a, b):
    wins = [
        ('A', 'Y'),
        ('B', 'Z'),
        ('C', 'X')
    ]

    shape_score = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3 }

    def win_score():
        if shape_score[a] == shape_score[b]:
            return 3
        if (a, b) in wins:
            return 6
        return 0
    
    return win_score() + shape_score[b]

total_score = 0
for line in sys.stdin:
    a, b = line.split()
    total_score += score(a, b)
print(total_score)
