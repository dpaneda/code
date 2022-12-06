import sys
import re
from operator import add, mul

def tokenize(s):
    s += ' '
    l = []
    deep = 0
    i = 0
    for j in range(len(s)):
        if s[j] == ' ':
            if deep == 0 and s[i:j]:
                l.append(s[i:j])
                i = j + 1
        elif s[j] == '(':
            deep += 1
        elif s[j] == ')':
            deep -= 1
            if deep == 0:
                l.append(s[i+1:j])
                i = j + 2
    return l

def eval_expr(s):
    tokens = tokenize(s)
    tokens = eval_sums(s)
    n = 0
    op = add
    for token in tokens:
        if token.isdigit():
            n = op(n, int(token))
        elif token == '*':
            op = mul
        else:
            n = op(n, eval_expr(token))
    return n

def eval_sums(s):
    tokens = tokenize(s)
    nt = []
    op = None
    for token in tokens:
        if token.isdigit():
            if op:
                n = op(int(n), int(token))
            else:
                n = token
        elif token == '+':
            op = add
        elif token == '*':
            nt.append(str(n))
            nt.append('*')
            op = None
        else:
            if op:
                n = op(int(n), eval_expr(token))
            else:
                n =  eval_expr(token)
    if n:
        nt.append(str(n))
    return nt

n = 0
for line in sys.stdin:
    n += eval_expr(line.strip())
print(n)
