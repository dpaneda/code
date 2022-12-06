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

def run(code):
    acc = ip = 0
    breadcrumbs = set()

    while ip < len(code):
        if ip in breadcrumbs:
            return False
        breadcrumbs.add(ip)
        inst, op = code[ip]
    
        #print(f"{inst} {op}")
        if inst == 'nop':
            ip += 1
        elif inst == 'jmp':
            ip += op
        elif inst == 'acc':
            acc += op
            ip += 1
    return acc

for i in range(0, len(code)):
    inst, op = code[i]
    code2 = list(code)
    if inst == 'nop':
        code2[i] = ('jmp', op)
    elif inst == 'jmp':
        code2[i] = ('nop', op)
    else:
        continue
    acc = run(code2)
    if acc != False:
        break

print(acc)
