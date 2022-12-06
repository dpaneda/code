from collections import deque

starting_cups = "389125467"
starting_cups = "643719258"
cups = [int(c) for c in starting_cups]
cups += range(1 + len(cups), 1000001)
cups = deque(cups)

last = 0

def find_target(cups, target, last):
    for i in [2, 5, 10, 50, 100, 1000]:
        try:
            j = cups.index(target, last - i, last + i)
            return j
        except ValueError:
            continue
    return cups.index(target)

def step(cups):
    global last
    l = []

    current = cups[0]
    cups.rotate(-1)
    #print(cups, current, pick)
    #print(f"From: {pick}")
    for _ in range(3):
        l.append(cups.popleft())
    target = None
    candidate = current - 1
    while candidate >= 1:
        if candidate not in l:
            target = candidate
            break
        candidate -= 1
    if not target:
        target = max(cups)
#    try:
#        i = cups.index(target, last - 10, last + 10) + 1
#    except ValueError:
#        i = cups.index(target) + 1
#        print(f"BAD {i} {last}")
    i = find_target(cups, target, last) + 1
    last = i
    #print(f"Moving a, b, c {pick} => {i}")
    #print(target, i)
    cups.insert(i, l.pop())
    cups.insert(i, l.pop())
    cups.insert(i, l.pop())
    #print(cups, target, l)
    return cups

for _ in range(10000000):
    cups = step(cups)
i = cups.index(1)
cups.rotate(-i)
print(cups[0], cups[1], cups[2])
#cups = cups[i+1:] +  cups[:i]
#print("".join(map(str, cups)))
