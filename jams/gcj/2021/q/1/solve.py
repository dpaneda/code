def solve():
    _ = input()
    l = list(map(int, input().split()))
    
    cost = 0
    while len(l) > 1:
        j = l.index(min(l))
        cost += j + 1
        l = l[j::-1] + l[j+1:]
        l.pop(0)
    return cost

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
