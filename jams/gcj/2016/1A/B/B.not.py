#!/usr/bin/python3

import sys

def check_army(army):
    for l in army:
        if not all(x <= y for x,y in zip(l, l[1:])):
            return False

def valid_row(army, l, row):
    n = len(army)
    army = list(army)
    army[row] = l
    return check_army(army)

#    for i in range(0, n):
#        j = i
#        while army[row - 1][i] == 0:
#        if row > 0 and army[row - 1][i] != 0 and l[i] <= army[row - 1][i]:
#            return False
#        if row < n - 1 and army[row + 1][i] and l[i] >= army[row + 1][i]:
#            return False
#        if army[row][i] != 9 and l[i] != army[row][i]:
#            return False
#    print("Valid row:", l, row)
#    return True

def valid_col(army, l, col):
    n = len(army)
    for i in range(0, n):
        if col > 0 and army[i][col - 1] != 0 and l[i] <= army[i][col - 1]:
#            print(l[i],"<=",army[i][col - 1])
            return False
        if col < n - 1 and army[i][col + 1] != 0 and l[i] >= army[i][col + 1]:
#            print(l[i],">=",army[i][col + 1])
            return False
#        if army[i][col] != 9 and l[i] != army[i][col]:
#            return False
#    print("Valid col:", l, col)
    return True

def set_army(army, what, l):
    n = len(army)
    kind, k = what
    if kind == 'row':
        for i in range(0, n):
            army[k][i] = l[i] 
    else:
        for i in range(0, n):
            army[i][k] = l[i] 
    print_army(army)

def search(army, l, rows, cols):
    valids = []
    for row in rows:
        if valid_row(army, l, row):
            valids.append(['row', row])
    for col in cols:
        if valid_col(army, l, col):
            valids.append(['col', col])
    print("Valids:", l, len(valids))
    if len(valids) == 1:
        set_army(army, valids[0], l)
        return valids[0]
    return None

def print_army(army):
    for l in army:
        l = map(str, l)
        print(" ".join(l))

#def min_army(army):
#    n = 0
#    min = 9999
#    for i in range(0, len(army)):
#        if army[i][0] != 0 and < min:
#            min = army[i][0]
#            n = i
#    return n

def solve():
    n = int(input())
    soldiers = []
    for _ in range(1, 2*n):
        l = list(map(int,input().split()))
        soldiers.append(l)
    army = []
    for i in range(0, n):
        army.append([0] * n)
#    m = min_army(army)
    soldiers.sort()
    l = soldiers.pop(0)
    army[0] = l

    print_army(army)

    for s in soldiers:
        s = map(str, s)
        print(" ".join(s))
    
    rows = list(range(1, n))
    cols = list(range(0, n))

    while len(rows + cols) > 1:
        print(len(rows + cols))
        for l in soldiers:
            v = search(army, l, rows, cols)
            if v:
                print(rows, cols, v)
                soldiers.remove(l)
                if v[0] == 'row':
                    rows.remove(v[1])
                else:
                    cols.remove(v[1])

num = int(sys.stdin.readline())
for case in range(1, num + 1):
    print("Case #{0}: {1}".format(case, solve()))
