#!/usr/bin/python

import sys
import subprocess

def gen_problem():
    T = int(raw_input())
    P = int(raw_input())
    S = int(raw_input())

    available_time = []
    trees_time = []
    for i in xrange(P):
        l = map(int, sys.stdin.readline().split())
        available_time.append(l[0])
        trees_time.append(l[1:])

    # min: 10 l1a1 + 20 l1a2 + 20 l2a1 + 10 l2a2;
    s = "min: 0"
    for p in xrange(P):
        for t in xrange(T):
            s += " + {0} l{1}a{2}".format(trees_time[p][t], p, t)
    s += ";\n\n"

    for t in xrange(T):
        s += "0 "
        for p in xrange(P):
            s += " + l{0}a{1}".format(p, t)
        s += " = 1;\n";

    s += "\n"

    for p in xrange(P):
        s += "0 "
        for t in xrange(T):
            s += " + {0} l{1}a{2}".format(trees_time[p][t], p, t)
        s += " <= {0};\n".format(available_time[p]);

    s += "\n"

    for p in xrange(P):
        for t in xrange(T):
            s += "0 <= l{0}a{1};\n".format(p, t)

    return S, s

n = int(sys.stdin.readline())

for i in xrange(n):
    S, problem = gen_problem()
    p = subprocess.Popen(["lp_solve", "-S1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
    p.stdin.write(problem)
    p.stdin.close()
    solution = p.stdout.readlines()
    if len(solution) < 2:
        output = "NO"
    else:
        pos = 2 + solution[1].strip().find(":")
        x = float(solution[1][pos:])
        delta = int(round(x - S))
        if delta == 0:
            output = "OK"
        else:
            output = str(delta)

    print output
