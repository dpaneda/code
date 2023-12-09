#! /usr/bin/env python

import sys

def distance(time, charge):
    return (time - charge) * charge

time = int(''.join(filter(lambda c: c.isdigit(), input())))
max_distance = int(''.join(filter(lambda c: c.isdigit(), input())))

options = filter(lambda i: distance(time, i) > max_distance, range(time))
print(len(list(options)))
