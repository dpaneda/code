#!/usr/bin/python
import sys

def check_strings(a, b, ai, bi):
    longest = ""
    actual = ""
    while ai < len(a) and bi < len(b):
        if a[ai] == b[bi]:
            actual = actual + a[ai]
            if len(actual) > len(longest):
                longest = actual
        else:
            actual = ""
        ai, bi = ai + 1, bi + 1
    return longest
    
def solve(a, b):
    offset = 0
    longest = ""
    while offset < len(a) or offset < len(b):
        actual = check_strings(a, b, offset, 0)
        if len(actual) > len(longest):
            longest = actual
        actual = check_strings(a, b, 0, offset)
        if len(actual) > len(longest):
            longest = actual
        offset += 1
    return longest

for line in sys.stdin:
    a, b = line.split()
    print solve(a, b)
