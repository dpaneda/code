import sys

l = []
preamble = set()
a, b = 0, 25

for line in sys.stdin:
    l.append(int(line))

for i in range(0, 25):
    preamble.add(l[i])

def valid(preamble, n):
    for n2 in preamble:
        if n - n2 in preamble and n2 != n / 2:
            return True
    return False

i = 25
while i < len(l):
    if not valid(preamble, l[i]):
        break
    preamble.remove(l[i - 25])
    preamble.add(l[i])
    i += 1

target = l[i]
print(target)

a = 0
b = 1

while True:
    s = sum(l[a:b])
    if s == target:
        break
    elif s < target:
        b += 1
    elif s > target:
        a += 1

print(min(l[a:b]) + max(l[a:b]))
