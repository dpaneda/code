import itertools

def construct(n, c):
    #print(n, c)
    #if c < n - 1:
    #    return "IMPOSSIBLE"
    #if c > (n * (n-1) / 2):
    #    return "IMPOSSIBLE"

    c -= n - 1 
    if c < 0:
        return "IMPOSSIBLE"
    l = []
    for i in range(n, 0, -1):
        if c == 0:
            l = [i] + l
        elif c >= len(l):
            c -= len(l) 
            l = l[::-1] + [i]
        else:
            l = l[c-1::-1] + [i] + l[c:]
            c = 0
    #    print(l)
    if c > 0:
        return "IMPOSSIBLE"
    #print(cost(l))

    return " ".join(map(str,l))
            

def cost(l):
    cost = 0
    while len(l) > 1:
        j = l.index(min(l))
        cost += j + 1
        l = l[j::-1] + l[j+1:]
        l.pop(0)
    return cost

def solve():
    n, c = list(map(int, input().split()))
    
    return construct(n, c)

    found = False
    for p in itertools.permutations(range(1, n+1)):
        l = list(p)
        if cost(l) == c:
            return " ".join(map(str,l))
    return "IMPOSSIBLE"

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
