#!/usr/bin/python2

import sys

table = {}
table['1'] = {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'}
table['i'] = {'1': 'i', 'i': '1', 'j': 'k', 'k': 'j'}
table['j'] = {'1': 'j', 'i': 'k', 'j': '1', 'k': 'i'}
table['k'] = {'1': 'k', 'i': 'j', 'j': 'i', 'k': '1'}

neg = {}
neg['1'] = {'1': False, 'i': False, 'j': False, 'k': False}
neg['i'] = {'1': False, 'i': True,  'j': False, 'k': True}
neg['j'] = {'1': False, 'i': True,  'j': True,  'k': False}
neg['k'] = {'1': False, 'i': False, 'j': True,  'k': True}

cache = {}


def qmul(s, i, n=None):
    negative = False

    if not n:
        n = len(s)

    acc = s[i]
    for c in s[i + 1:n]:
        if neg[acc][c]:
            negative = not negative
        acc = table[acc][c]

    if negative:
        ret = None
    else:
        ret = acc

    return ret


def qmul_cache(s, i, n=None):
    global cache
    negative = False

    if not n:
        n = len(s)

    if i in cache:
        return cache[i]

    acc = s[i]
    for c in s[i + 1:n]:
        if neg[acc][c]:
            negative = not negative
        acc = table[acc][c]

    if negative:
        cache[i] = None
    else:
        cache[i] = acc

    return cache[i]


def qmul_until(s, target, acc, start):
    negative = False
    for i in xrange(start, len(s)):
        c = s[i]
        if neg[acc][c]:
            negative = not negative
#        print "{0} {1} => {2}".format(acc, c, table[acc][c])
        acc = table[acc][c]
        if not negative and acc == target:
            return i + 1

    return None


def solve():
    global cache
    L, K = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    #s = s * K

#    print s
    cache = {}

    if len(s) < 3:
        return "NO"

    if s[0] == 'i':
        i_split = 1
    else:
        i_split = qmul_until(s, 'i', s[0], 1)

    while i_split:
#        print "i: {0}".format(i_split)
        if s[i_split] == 'j':
#            print "DIRECT"
            j_split = i_split + 1
        else:
            j_split = qmul_until(s, 'j', s[i_split], i_split + 1)

        while j_split and j_split < len(s):
            if qmul_cache(s, j_split) == 'k':
#                print i_split, j_split
#                print qmul(s, 0, i_split)
#                print qmul(s, i_split, j_split)
                return "YES"

#            print "i_split {0}, j_split {1} i: {2} j: {3}".format(i_split, j_split, qmul(s, 0, i_split), qmul(s, i_split, j_split))
#            print s[i_split:j_split]
            j_split = qmul_until(s, 'j', 'j', j_split)
#            print s[i_split:j_split]
#            print "i_split {0}, j_split {1} i: {2} j: {3}".format(i_split, j_split, qmul(s, 0, i_split), qmul(s, i_split, j_split))

#            if not j_split or j_split >= len(s):
#                break

        i_split = qmul_until(s, 'i', 'i', i_split)

        if not i_split or i_split + 1 > len(s):
            return "NO"

    return "NO"

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
