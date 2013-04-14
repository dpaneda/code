#!/usr/bin/python2

import sys


def search_lock(chests, rchests, c, keys):
    if chests[c][0] in keys:
#        print("need for %d in keys" % c)
        return False

    for i in rchests:
        #print(i)
        #print(chests[i][1:])
        if c == i:
            continue
        if chests[c][0] in chests[i][1:]:
#            print("%d -> %d" % (c, i))
            nr = list(rchests)
            nr.remove(c)
            return search_lock(chests, nr, i, keys)
    return True


def check_path(path, keys, chests, nchests, rchests):
    for c in rchests:
        if chests[c][0] in keys:
            np = list(path)
            np.append(c)
            if len(np) == nchests:
                return np
            nk = list(keys)
            nk.remove(chests[c][0])
            nk += chests[c][1:]
            nr = list(rchests)
            nr.remove(c)

            p = check_path(np, nk, chests, nchests, nr)
            if p:
                return p
    return None


def Solve():
    k, n = map(int, sys.stdin.readline().split())
    keys = map(int, sys.stdin.readline().split())
    chests = {}
    for c in xrange(1, n + 1):
        chests[c] = map(int, sys.stdin.readline().split())
        del(chests[c][1])

#    print(keys)
#    for c in chests:
#        print chests[c]

    path = check_path([], keys, chests, len(chests), range(1, len(chests) + 1))
    if path:
        return ' '.join(map(str, path))

    return 'IMPOSSIBLE'

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
