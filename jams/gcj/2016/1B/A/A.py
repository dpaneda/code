#!/usr/bin/python3

names = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

search = [
    ('Z', 0),
    ('W', 2),
    ('X', 6),
    ('G', 8),
    ('H', 3),
    ('R', 4),
    ('F', 5),
    ('S', 7),
    ('O', 1),
    ('N', 9)
]


import sys
from collections import Counter

def solve():
    s = input()
    count = Counter(s)

    phone = ""

    for letter, number in search:
        while count[letter]:
            phone += str(number)
            for c in names[number]:
                count[c] -= 1

    return ''.join(sorted(phone))

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
