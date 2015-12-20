#!/usr/bin/python2

import sys
import operator


def factors(n):
    gaps = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6]
    length, cycle = 11, 3
    f, fs, next = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[next]
        next += 1
        if next == length:
            next = cycle
    if n > 1:
        fs.append(n)
    return fs


#def intersect(a, b):
#    return list(set(a) & set(b))

def intersect(a, b):
    setIn = set(a).intersection(set(b))
    rt = []
    for i in setIn:
        for j in range(min(a.count(i), b.count(i))):
            rt.append(i)
    return rt


def normalize(ages, K):
    if ages.count(0) > 0:
        while ages.count(0) > 1:
            ages[ages.index(0)] += K
        if max(ages) > K:
            ages[ages.index(0)] += K
    for i in xrange(0, len(ages)):
        if ages[i] % K:
            ages[i] += K - (ages[i] % K)
    return ages


def resolve_conflict(ages, i, j, K):
    fi = factors(ages[i])
    fj = factors(ages[j])
    fni = factors(ages[i] + K)
    fnj = factors(ages[j] + K)
    a = sum(intersect(fni, fj))
    b = sum(intersect(fnj, fi))
    if a < b:
        ages[i] += K
    else:
        ages[j] += K


def min_gifts(ages, K):
    ages = normalize(ages, K)

    conflict = True
    while conflict:
        conflict = False
        for i in xrange(0, len(ages)):
            for j in xrange(i + 1, len(ages)):
                mcd = intersect(factors(ages[i]), factors(ages[j]))
                if mcd and reduce(operator.mul, mcd) > K:
                    resolve_conflict(ages, i, j, K)
                    conflict = True
                elif False:
                    print ages[i], ages[j]
                    print factors(ages[i])
                    print factors(ages[j])
                    print intersect(factors(ages[i]), factors(ages[j]))
                    print sum(intersect(factors(ages[i]), factors(ages[j])))
    ages = normalize(ages, K)
    print ages
#    for n in ages:
#        print factors(n)
    return sum(ages)


def solve():
    N, K = map(int, sys.stdin.readline().split())
    ages = sorted(map(int, sys.stdin.readline().split()))
    tradition = sum(ages)
    return min_gifts(ages, K) - tradition

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, solve())
