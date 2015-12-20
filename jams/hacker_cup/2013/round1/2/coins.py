#!/usr/bin/python2

def solve():
    N, K, C = map(int, raw_input().split())
    for i in xrange(N, 0, -1):
        if not K % i:
            return C + N - i

num = int(raw_input())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, solve())
