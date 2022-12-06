#! /usr/bin/env python
cases = int(input())

for case in range(1, cases + 1):
    printers = []
    for _ in range(3):
        printers.append(list(map(int, input().split())))

    color = [0] * 4
    i = 0
    while sum(color) < 10**6 and i <= 3:
        n = min(printers[0][i], printers[1][i], printers[2][i])
        missing = 10 ** 6 - sum(color)
        color[i] = min(n, missing)
        i += 1
    if sum(color) == 10**6:
        print(f"Case #{case}: {' '.join(map(str, color))}")
    else:
        print(f"Case #{case}: IMPOSSIBLE")
