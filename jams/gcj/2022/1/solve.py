#! /usr/bin/env python
cases = int(input())
for case in range(1, cases + 1):
    print(f"Case #{case}:")
    R, C = map(int, input().split())
    grid = {}
    print(f"..{'+-' * (C-1)}+")
    print(f"..{'|.' * (C-1)}|")
    for _ in range(R-1):
        print(f"{'+-' * C}+")
        print(f"{'|.' * C}|")
    print(f"{'+-' * C}+")
