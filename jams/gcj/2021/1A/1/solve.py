def digits(n : int) -> int:
    return len(str(n))

def all_nines(n : int) -> bool:
    sn = str(n)
    return sn.count('9') == len(sn)

def solve():
    N = int(input())
    l = list(map(int, input().split()))

    def pick_next(a: int, b: int) -> int:
        if a < b:
            return b

        if digits(a) == digits(b):
            return b * 10
        
        # a should have more digits than b
        sa, db = str(a), digits(b)
        prefix, rest = int(sa[:db]), sa[db:]
        needed_zeroes = len(rest)
        #print(prefix, b, rest, needed_zeroes)
        nb = b * 10**needed_zeroes
    
        if prefix < b:
            return nb
        elif prefix > b:
            return nb * 10

        # b starts exactly like a
        if all_nines(int(rest)):
            return nb * 10
        else:
            nb += int(rest) + 1
            return nb
    
    n1 = l.pop(0)
    nl = [n1]
    c = 0
    while l:
        n2 = l.pop(0)
        new_n2 = pick_next(n1, n2)
        c += len(str(new_n2)) - len(str(n2))
        nl.append(new_n2)
        n1 = new_n2
    print(nl)
    return c


cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
