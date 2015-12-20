import sys

def search_n(n):
    m = n + 1
    while True:
        for i in range(2, n + 1):
            if m % i:
                break
        if i != n or m % n:
            m += 1
            continue
        else:
            return m

cases = int(sys.stdin.readline())
for case in range(cases):
    print(search_n(int(sys.stdin.readline())))
