#! /usr/bin/env python

from functools import partial

def read_map(l):
    input()
    rules = []
    s = input().split()
    while len(s):
        l = list(map(int, s))
        rules.append(l)
        try:
            s = input().split()
        except EOFError:
            break

    def inverse_map(rules, n):
        for destination, source, size in rules:
            delta = source - destination
            if destination <= n < (destination + size):
                return n + delta
        return n
    return partial(inverse_map, rules)


def in_seeds(seeds, n):
    for i in range(0, len(seeds), 2):
        a, b = seeds[i:i+2]
        if a <= n <= a + b:
            return True
    return False

seeds = list(map(int, input().split(':')[1].split()))
input()

seed_maps = []

for _ in range(7):
    seed_maps.insert(0, read_map(seeds))

for i in range(100000000):
    n = i
    for f in seed_maps:
        n = f(n)
    if in_seeds(seeds, n):
        print(i)
        break
