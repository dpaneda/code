import sys

positions = None
numbers = []
for line in sys.stdin:
    l = list(line.strip())
    numbers.append(l)
    if not positions:
        positions = list(map(list, l))
    else:
        for i in range(len(l)):
            positions[i].append(l[i])

def winner(l, pos):
    k = 0
    for n in l:
        if n[pos] == '1':
            k += 1
        else:
            k -= 1
    if k >= 0:
        return '1'
    else:
        return '0'

oxygen = list(numbers)
i = 0
while len(oxygen) > 1:
    k = winner(oxygen, i)
    oxygen = list(filter(lambda n : n[i] == k, oxygen))
    i += 1
    print(oxygen)

co = list(numbers)
print(co)
i = 0
while len(co) > 1:
    k = winner(co, i)
    co = list(filter(lambda n : n[i] != k, co))
    i += 1
    print(co)

a = int(''.join(oxygen[0]), 2)
b = int(''.join(co[0]), 2)
print(a * b)
