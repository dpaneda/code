#! /usr/bin/env python

import sys

def distance(time, charge):
    return (time - charge) * charge

times = list(map(int, input().split(':')[1].split()))
distances = list(map(int, input().split(':')[1].split()))

n = 1
for time, max_distance in zip(times, distances):
    options = filter(lambda i: distance(time, i) > max_distance, range(time))
    n *= len(list(options))
print(n)
