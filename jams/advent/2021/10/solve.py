#! /usr/bin/env python
import sys

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

def check_line(line) -> int:
    stack = []
    for c in line.strip():
        if c in pairs:
            c2 = stack.pop()
            if pairs[c] != c2:
                print(f"Found {c} with {c2} on stack")
                return points[c]
        else:
            stack.append(c)
    return 0

score = 0
for line in sys.stdin:
    score += check_line(line)
print(score)
