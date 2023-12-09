#! /usr/bin/env python

def process_map(l):
    input()
    s = input().split()
    l2 = list(l)
    while len(s):
        destination, source, size = map(int, s)
        delta = destination - source
        for i, n in enumerate(l):
            if source <= n < (source + size):
                l2[i] = n + delta
        try:
            s = input().split()
        except EOFError:
            break
    return l2


seeds = list(map(int, input().split(':')[1].split()))
input()

seed_maps = []
for _ in range(7):
    seeds = process_map(seeds)
print(min(seeds))
