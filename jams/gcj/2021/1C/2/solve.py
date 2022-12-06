import math

def search_year(n, actual, digits):
    year = actual
    while year <= n:
        year = year * (10 ** digits)
        actual += 1
        year += actual
    return year

def search_year_iterate(n, digits):
    min_year = 10**19
    for actual in range(10**(digits-1), 10**digits):
        year = search_year(n, actual, digits)
        if year < min_year:
            #print(actual, digits, year, min_year)
            min_year = year
    return min_year

def solve():
    Y = int(input())

    min_year = 10**19
    digits = digits = int(math.log10(Y)) + 1
    for d in range(1, 1 + (digits // 2)):
        year = search_year_iterate(Y, d)
        if year < min_year:
            min_year = year
    return min_year

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
