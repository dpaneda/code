def play(l, k):
    l, k = list(l), list(k)
    print("Play", l, k)
    while l and k:
        if l[0] > k[0]:
            l.append(l.pop(0))
            l.append(k.pop(0))
        else:
            k.append(k.pop(0))
            k.append(l.pop(0))
    return l + k

def score(l):
    n = 0
    while l:
        print(len(l), l[0], n)
        n += len(l) * l.pop(0)
    return n

games = set()

def combat(l, k):
    while l and k:
        cid = str(l) + str(k)
        if cid in games:
            return 1
        else:
            games.add(cid)
        a, b = l.pop(0), k.pop(0)
        if a <= len(l) and b <= len(k):
            winner = play_fast(l[:a], k[:b])
        else:
            winner = 1 if a > b else 2
        if winner == 1:
            l.append(a)
            l.append(b)
        else:
            k.append(b)
            k.append(a)
        print(l, k, winner)
    print(l + k)
    return 1 if l else 2

l = list(map(int, input().split()))
k = list(map(int, input().split()))
print(score(play(l, k)))
#winner = combat(l, k)
#print(winner)
#print(score(l) if winner == 1 else score(k))
