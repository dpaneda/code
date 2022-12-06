#! /usr/bin/env python
import sys

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
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
                return 0
        else:
            stack.append(c)
            
    score = 0
    while stack:
        c = stack.pop()
        score *= 5
        score += points[c]
    return score

scores = []
for line in sys.stdin:
    score = check_line(line)
    if score:
        scores.append(score)
scores.sort()
print(scores[len(scores) // 2])
