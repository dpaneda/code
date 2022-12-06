cups = [int(c) for c in input()]

def step(cups, current):
    print(cups, current)
    l = []
    pick = cups.index(current) + 1
    for _ in range(3):
        pick = pick % len(cups)
        l.append(cups.pop(pick))
    target = None
    candidate = current - 1
    while candidate >= 1:
        if candidate in cups:
            target = candidate
            break
        candidate -= 1
    if not target:
        target = max(cups)
    i = cups.index(target)
    print(cups, target, l, i)
    cups = cups[:i + 1] + l + cups[i + 1:]
    #print(cups, target, l)
    next_index = (cups.index(current) + 1) % len(cups)
    current = cups[next_index]
    return cups, current

current = cups[0]
for _ in range(100):
    cups, current = step(cups, current)
i = cups.index(1)
cups = cups[i+1:] +  cups[:i]
print("".join(map(str, cups)))
