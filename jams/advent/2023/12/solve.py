#! /usr/bin/env python

import sys


def group_count(s):
    ZQ

def arrangements(s):
    def parse(s):
        sgroups, scounts = s.split()
        groups = ['']
        for c in sgroups:
            if c == '.':
                if groups and groups[-1] != '':
                    groups.append('')
                continue
            if groups[-1] == '' or groups[-1][-1] == c:
                groups[-1] +=c
            else:
                groups.append(c)
        counts = [int(i) for i in scounts.split(',')]
        print(groups, counts)

    parse(s)

for line in sys.stdin:
    arrangements(line)

