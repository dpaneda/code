#!/usr/bin/python

import sys

def resolve_task(task):
    global durations
    global dependencies
    m = 0
    if dependencies.has_key(task):
        times = map(resolve_task, dependencies[task])
        m = max(times)
    return m + durations[task]
        
f = open("in", "r")
mode = 0

durations = {}
dependencies = {}

for line in f:
    if line.strip() == "#Task duration":
        mode = 1
    elif line.strip() == "#Task dependencies":
        mode = 2
    elif mode == 1 and len(line) > 3:
        a, b = map(int, line.split(','))
        durations[a] = int(b)
    elif mode == 2 and len(line) > 3:
        tasks = map(int, line.split(','))
        dependencies[tasks[0]] = tasks[1:]

numbers = map(int, sys.stdin.readline().split(','))
for n in numbers:
    print "%d %d" % (n, resolve_task(n))
