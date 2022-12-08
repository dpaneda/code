#! /usr/bin/env python

import re, sys
import pprint

tree = {}
pwd = []

def add_file(name, size):
    t = tree
    for d in pwd:
        t = t[d]
    if size == 'dir':
        t[name] = {}
    else:
        t[name] = int(size)

def calculate_sizes(t):
    size = 0
    for k, v in t.items():
        if type(v) is dict:
            size += calculate_sizes(v)
        else:
            size += v
    t['.'] = size
    return size

def find_small_dirs(t):
    size = 0
    for k, v in t.items():
        if type(v) is dict:
            size += find_small_dirs(v)
    if t['.'] <= 100000:
        size += t['.']
    return size

def find_best_dir(t, delete_size):
    size = 0
    best_size = 70000000
    for k, v in t.items():
        if type(v) is dict:
            best_size = min(best_size, find_best_dir(v, delete_size))
    if t['.'] >= delete_size and t['.'] < best_size:
        best_size = t['.']
    return best_size

for line in sys.stdin:
    m = re.search('\$ cd (.+)', line)
    if m:
        match m[1]:
            case '..':
                pwd.pop()
            case '/':
                pwd = []
            case _:
                pwd.append(m[1])
    if line[0] != '$':
        size, name = line.split()
        add_file(name, size)

usage = calculate_sizes(tree)
free_size = 70000000 - usage
delete_size = 30000000 - free_size

pprint.pprint(tree)
print(find_best_dir(tree, delete_size))
