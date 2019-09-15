def solve():
    P, Q = map(int, raw_input().split())
    v = []
    for p in xrange(P):
        line = raw_input().split()
        x, y = map(int, line[0:2])
        if line[2] == 'N':
            f = lambda a, b, n=y : b > n
        elif line[2] == 'S':
            f = lambda a, b, n=y : b < n
        elif line[2] == 'W':
            f = lambda a, b, n=x : x < n
        elif line[2] == 'E':
            f = lambda a, b, n=x : x > n
        v.append(f)

    bestx, bestxvalue = 0, 0
    for x in xrange(0, Q+1):
        hits = [f(x, 0) for f in v].count(True)
        if hits > bestxvalue:
            bestx, bestxvalue = x, hits

    besty, bestyvalue = 0, 0
    for y in xrange(0, Q+1):
        hits = [f(0, y) for f in v].count(True)
        if hits > bestyvalue:
            besty, bestyvalue = y, hits

    if bestxvalue > bestyvalue:
        besty, bestyvalue = 0, 0
        for y in xrange(0, Q+1):
            hits = [f(bestx, y) for f in v].count(True)
            if hits > bestyvalue:
                besty, bestyvalue = y, hits
    else:
        bestx, bestxvalue = 0, 0
        for x in xrange(0, Q+1):
            hits = [f(x, besty) for f in v].count(True)
            if hits > bestxvalue:
                bestx, bestxvalue = x, hits
    return "{} {}".format(bestx, besty)

cases = input()
for case in xrange(1, cases + 1):
    print "Case #{}: {}".format(case, solve())
