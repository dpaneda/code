#!/usr/bin/python2

import re
import sys
import subprocess


def solve():
    line = sys.stdin.readline().split()
    N = int(line[0])
    V = float(line[1])
    X = float(line[2])
    R = []
    C = []
    for _ in xrange(N):
        r, c = map(float, sys.stdin.readline().split())
        R.append(r)
        C.append(c)

#    print N, V, X
#    for r in R:
#        print r
#    for c in C:
#        print c

    if max(C) < X or min(C) > X:
        return 'IMPOSSIBLE'

#    ve = 0
#    for i in xrange(N):
#        if abs(C[i] - X) < 0.000001:
#            ve += R[i]
#    if ve > 0:
#        return V / ve

    s = "Minimize\ntime\nSubject To\n"
    for n in xrange(N):
        s += "T{0} - time <= 0\n".format(n)
        s += "T{0} >= 0\n".format(n)
    for n in xrange(N):
        s += " + {0} T{1}".format(R[n], n)
    s += " = {0}\n".format(V)

    for n in xrange(N):
        s += " + {0} T{1}".format(R[n] * C[n] / V, n)
    s += " = {0}\n".format(X)
    s += "End"

    p = subprocess.Popen(["glpsol", "--lp", "--nomip", "-w", "glp_sol", "/dev/stdin"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
    p.stdin.write(s)
    p.stdin.close()
    print p.stdout.readlines()
    sol = float(open("glp_sol").readlines()[1].split()[-1])
    if sol > 0:
        return sol
    return "IMPOSSIBLE"

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print "Case #{0}: {1}".format(case, solve())
