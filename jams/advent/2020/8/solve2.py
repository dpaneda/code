import sys

acc = 0
code = []
for line in sys.stdin:
    line = line.split(' ')
    code.append((line[0], int(line[1])))

breadcrumbs = set()

ip = 0
while ip <= len(code):
    if ip in breadcrumbs:
        break
    breadcrumbs.add(ip)
    inst, op = code[ip]
    if inst == 'nop':
        ip += 1
    elif inst == 'jmp':
        ip += op
    elif inst == 'acc':
        acc += op
        ip += 1

print(acc)
