def solve():
    l = []
    n = int(input())
    for _ in range(n):
        l.append(list(map(int, input().split())))
        
    total = sum(range(1, n+1))
    trace = 0
    bad_rows = 0
    bad_cols = 0
    
    for i in range(n):
        trace += l[i][i]
        row = set(l[i])
        col = set()
        for j in range(n):
            col.add(l[j][i])
        if len(row) != n or sum(row) != total:
            bad_rows += 1
        if len(col) != n or sum(col) != total:
            bad_cols += 1
    return "{} {} {}".format(trace, bad_rows, bad_cols)
    

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
