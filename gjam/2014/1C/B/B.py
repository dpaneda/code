#!/usr/bin/python2

import sys
import math


def noway(trains):
    letters = count_letters(trains)
    for t in trains:
        if not valid_train(t):
            return True
        for i in xrange(1, len(t) - 1):
            c = t[i]
            if t.count(c) < letters[c] and c != t[0] and c != t[1]:
                return True
    return False


def find_rules(trains):
    index = letter_index(trains)
    letters = count_letters(trains)
    rules = {}
    for i in xrange(0, len(trains)):
        last = trains[i][-1]
#        if trains[i].count(last) == len(trains[i]):
            # Single letter train
#            continue
        if trains[i].count(last) == letters[last]:
            # Single train with this letter
            continue
        if last not in index:
            return False
        if i in index[last]:
            # Same train, loop in rules
            if len(index[last]) == 1:
                continue
            l = index[last]
            l.remove(i)
            rules[i] = l
        else:
            rules[i] = index[last]
    return rules


def count_letters(trains):
    letters = {}
    for t in trains:
        for c in t:
            if c not in letters:
                letters[c] = 0
            letters[c] += 1
    return letters


def letter_index(trains):
    index = {}
    for i in xrange(0, len(trains)):
        c = trains[i][0]
        if c not in index:
            index[c] = []
        index[c].append(i)
    return index


def valid_train(train):
    l = []
    actual = None
    for c in train:
        if c == actual:
            continue
        else:
            actual = c
            if c in l:
                return 0
            else:
                l.append(c)
    return 1


def count_ways(trains, actual_train):
    if len(trains) == 0:
        return 1

    if len(trains) == 1:
        return valid_train(actual_train + trains[0])

    c = 0
    for i in xrange(0, len(trains)):
        trains2 = list(trains)
        c += count_ways(trains2, actual_train + trains2.pop(i))
    return c


def apply_rules(trains):
    changed = True
    while changed:
        changed = False
        if noway(trains):
            return False, 0
        rules = find_rules(trains)
        if rules is False:
            return False, 0
        for k, v in rules.iteritems():
            if len(v) == 1:
                t1 = trains[k]
                t2 = trains[v[0]]
                trains.remove(t1)
                trains.remove(t2)
                trains.append(t1 + t2)
                changed = True
                break

    ruled = set()
    for k, v in rules.iteritems():
        ruled.add(k)
        ruled.union(set(v))

    free_trains = 0
    ruled_trains = []

    for i in xrange(0, len(trains)):
        if i in ruled:
            ruled_trains.append(trains[i])
        else:
            free_trains += 1

    return ruled_trains, free_trains


def solve():
    sys.stdin.readline()
    trains = sys.stdin.readline().split()
    trains, free_trains = apply_rules(trains)
    if trains is False:
        return 0
    if len(trains):
        c = count_ways(trains, "")
        c *= math.factorial(free_trains + 1)
    else:
        c = math.factorial(free_trains)
    return c % 1000000007


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, solve())
