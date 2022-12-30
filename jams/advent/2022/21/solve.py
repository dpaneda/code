#! /usr/bin/env python
import sys

expr = {}

def eval_expr_human(v, humn = 0):
    def eval_expr(v):
        if humn: 
            if v == 'root':
                v1, op, v2 = expr[v].split()
                a, b = eval_expr(v1), eval_expr(v2)
                return eval_expr(v1) - eval_expr(v2) 
            if v == 'humn':
                return humn
        match expr[v].split():
            case [v1, '+', v2]:
                return eval_expr(v1) + eval_expr(v2)
            case [v1, '-', v2]:
                return eval_expr(v1) - eval_expr(v2)
            case [v1, '*', v2]:
                return eval_expr(v1) * eval_expr(v2)
            case [v1, '/', v2]:
                return eval_expr(v1) / eval_expr(v2)
            case [n]:
                return int(n)
    return eval_expr(v)

def search_humn():
    humn_range = [1, 10**14]
    while True:
        humn = sum(humn_range) // 2
        diff = eval_expr_human('root', humn)
        if diff > 0:
            humn_range[0] = humn
        elif diff < 0:
            humn_range[1] = humn
        else:
            return humn

for line in sys.stdin:
    var, e = line.strip().split(': ')
    expr[var] = e

print(int(eval_expr_human('root')))
humn = search_humn()
print(humn)
