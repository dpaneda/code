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
    print(tokens)
    n = 0
    op = add
    print(tokens)
    for token in tokens:
        if token.isdigit():
            n = op(n, int(token))
        elif token == '+':
            op = add
        elif token == '*':
            op = mul
        else:
            #token = token[1:-1]
            n = op(n, eval_expr(token))
    #print(n)
    return n

n = 0
for line in sys.stdin:
    n += eval_expr(line.strip())
print(n)
