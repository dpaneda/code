def score(l):
    n = 0
    while l:
        n += len(l) * l.pop(0)
    return n

def combat(l, k):
    games = set()
    while l and k:
        cid = str(l) + str(k)
        if cid in games:
            return 1, 0
        games.add(cid)

        a, b = l.pop(0), k.pop(0)
        if a <= len(l) and b <= len(k):
            winner, _ = combat(l[:a], k[:b])
        else:
            winner = 1 if a > b else 2
        if winner == 1:
            l += [a, b]
        else:
            k += [b, a]
    return winner, score(l + k)

l = [int(s) for s in input().split()]
k = [int(s) for s in input().split()]
print("Winner {0}, Score: {1}".format(*combat(l, k)))
