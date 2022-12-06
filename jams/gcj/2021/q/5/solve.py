def solve():
    activities = []
    i = 0
    for _ in range(int(input())):
        a, b = map(int, input().split())
        activities.append((a, b, i))
        i += 1
    activities.sort()

    cameron = 0,0
    jaime = 0,0

    sched = [None] * len(activities)
    for a,b,i in activities:
        if a >= cameron[1]:
            cameron = a, b
            sched[i] = 'C'
        elif a >= jaime[1]:
            jaime  = a, b
            sched[i] = 'J'
        else:
            return 'IMPOSSIBLE'
    return ''.join(sched)

cases = int(input())
for case in range(1, cases + 1):
    print("Case #{}: {}".format(case, solve()))
