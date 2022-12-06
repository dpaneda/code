from itertools import permutations

SECOND = 10**9
MINUTE = SECOND * 60
HOUR = MINUTE * 60

def solve():
    l = list(map(int, input().split()))
    perms = permutations([0, 1, 2])

    def good(hours, minutes, seconds):
        nanoseconds = hours
        nanoseconds = nanoseconds % HOUR
        if nanoseconds * 12 != minutes:
            return False
        nanoseconds = nanoseconds % MINUTE
        if nanoseconds * 720 != seconds:
            return False
        return True

    def rotate_good(hours, minutes, seconds):
        for i in range(86400):
            hours   += i * SECOND
            minutes += i * SECOND * 12
            seconds += i * SECOND * 720
            hours   /= 43200000000000
            minutes /= 43200000000000
            seconds /= 43200000000000
            if good(hours, minutes, seconds):
                return resolve(hours, minutes, seconds)
        return False


    def resolve(hours, minutes, seconds):
        return hours // HOUR, minutes // (MINUTE * 12), seconds // (SECOND * 720), seconds % (SECOND * 720)
    
    for p in perms:
        a, b, c = p
        hours, minutes, seconds = l[a], l[b], l[c]
        r = rotate_good(hours, minutes, seconds)
        if r:
            print(r)
        #if good(hours, minutes, seconds):
        #    r = resolve(hours, minutes, seconds)
            return f"{r[0]} {r[1]} {r[2]} {r[3]}"


cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
