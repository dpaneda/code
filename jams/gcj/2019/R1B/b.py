def solve():
    N, K = map(int, raw_input().split())
    C = map(int, raw_input().split())
    D = map(int, raw_input().split())

    def valid(a, b):
        diff = abs(max(C[a:b+1]) - max(D[a:b+1]))
        return diff <= K

    res = 0
    for i in xrange(N):
        for j in xrange(i, N):
            if valid(i, j):
                res += 1
    return res

cases = input()
for case in xrange(1, cases+1):
    print("Case #{}: {}".format(case, solve()))
