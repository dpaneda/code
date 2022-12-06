def solve():
    nest = 0
    s = ""
    for d in map(int, list(input().strip())):
        if d > nest:
            s += '(' * (d - nest)
        elif d < nest:
            s += ')' * (nest - d)
        nest = d
        s += str(d)
    s += ')' * nest
    return s

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
