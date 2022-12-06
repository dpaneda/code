def crack_loops(public_key):
    n = 1
    i = 1
    while i:
        n = (n * 7) % 20201227
        if n == public_key:
            return i
        i += 1

def loop(subject, loops):
    n = 1
    for _ in range(0, loops):
        n = (n * subject) % 20201227
    return n


n2 = int(input())
n = int(input())

print(loop(n, crack_loops(n2)))
