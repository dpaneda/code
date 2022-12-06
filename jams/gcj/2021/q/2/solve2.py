def solve():
    x, y, s = input().split()
    cj, jc = map(int, [x, y])

    s = s.replace('?','')
    return cj * s.count('CJ') + jc * s.count('JC')

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
