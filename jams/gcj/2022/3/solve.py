#! /usr/bin/env python

def find_max(dices):
    i = 1
    while dices:
        if dices.pop() >= i:
            i += 1
        else:
            continue
    return i - 1

cases = int(input())
for case in range(1, cases + 1):
    input()
    dices = map(int, input().split())
    dices = sorted(dices, reverse=True)
    print(f"Case #{case}: {find_max(dices)}")
