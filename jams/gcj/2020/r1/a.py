import operator

def search(x, y, limit, searchs, used):
    n = 1
    while n < limit:
        keys = list(searchs.keys())
        for s in keys:
            if n in used[s]:
                continue
            searchs[s + 'N'] = tuple(map(operator.add, searchs[s], (0, n)))
            searchs[s + 'S'] = tuple(map(operator.add, searchs[s], (0, -n)))
            searchs[s + 'E'] = tuple(map(operator.add, searchs[s], (n, 0)))
            searchs[s + 'W'] = tuple(map(operator.add, searchs[s], (-n, 0)))
            used[s + 'N'] = used[s + 'S'] = used[s + 'E'] = used[s + 'W'] = used[s].union({n})
            del(searchs[s])
            del(used[s])
        for k, v in searchs.items():
            if v == (x, y):
                return k, used[k]
        n *= 2
    return None, None

def solve():
    x, y = map(int, input().split())
    m = 2 * max(map(abs, (x, y)))
    limit = 1
    while limit < m:
        limit *= 2
    searchs = {"": (0, 0)}
    used = {"": set()}
    s, u = search(x, y, limit, searchs, used)
    if not s:
        return "IMPOSSIBLE"
    else:
        return s
    
cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
