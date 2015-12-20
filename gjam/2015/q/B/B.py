#!/usr/bin/python2

import sys
import bisect


def special_minutes(dinners, added):
    best_time = max(dinners)
#    added = []
    dinners = list(dinners)
    best = list(dinners)
    best_added = list(added)
    minutes = 0

    for i in xrange(len(dinners)):
        m = dinners.pop()
        if m % 2 and m > 4 and (m, m - 1) in added:
            old_added = (m, m - 1)
            new_added = (m + 1, m - 2)
            added.remove(old_added)
            added.append(new_added)
            dinners.remove(m - 1)
            bisect.insort(dinners, m - 2)
            m += 1
        pick = m / 2
        bisect.insort(dinners, m - pick)
        bisect.insort(dinners, pick)
        minutes += 1
        current_time = minutes + max(dinners)
        added.append((m - pick, pick))
        if current_time < best_time:
            best = list(dinners)
            best_time = current_time
            best_added = list(added)

    return best, best_added


def split_all_da_things(dinners):
#    print dinners
#    total_added = 0
    old_added = 0
    dinners, added = special_minutes(dinners, [])
    while len(added) > old_added:
        dinners, added = special_minutes(dinners, added)
        old_added = len(added)
#        print dinners, added
#        total_added += len(added) / 2
    return dinners, len(added)


def solve():
    sys.stdin.readline()
    dinners = map(int, sys.stdin.readline().split())
    dinners.sort()

#    print dinners
    dinners, added = split_all_da_things(dinners)
#    print dinners
    return added + max(dinners)

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
