#!/usr/bin/python2

import sys


def is_locked(chests, rchests, c, keys):
#    print("searching for chest %d" % c)
#    print(rchests)
    if chests[c][0] in keys:
#        print("need for %d in keys" % c)
        return False

    for i in rchests:
        if c == i:
            continue
        if chests[c][0] in chests[i][1:]:
#            print("%d -> %d" % (c, i))
            nr = list(rchests)
            nr.remove(c)
            if not is_locked(chests, nr, i, keys):
                return False

#    print("CUT")
    return True


def check_path(path, keys, chests, nchests, rchests):
#    print("PATH:", path)
#    print("KEYS:", keys)
#    print("REMAIN:", rchests)

    needed_keys = []
    world_keys = list(keys)
    for c in rchests:
        needed_keys.append(chests[c][0])
        world_keys += chests[c][1:]

#    print("NEEDED:", needed_keys)
#    print("WORLD:", world_keys)
    if len(keys) < 1:
        return None

    for i in needed_keys:
        if i not in world_keys:
            return None
        world_keys.remove(i)

    for c in rchests:
        if is_locked(chests, rchests, c, keys):
            return None

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
        return ' '.join(map(str,path))

    return 'IMPOSSIBLE'

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
