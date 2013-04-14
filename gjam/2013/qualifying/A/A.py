#!/usr/bin/python2

import sys


def is_t_or_o(x):
    if x == 'T' or x == 'O':
        return True


def is_t_or_x(x):
    if x == 'T' or x == 'X':
        return True


def check_win(l):
    if len(filter(is_t_or_o, l)) == 4:
        return 'O won'
    if len(filter(is_t_or_x, l)) == 4:
        return 'X won'
    return None


def Solve():
    board = []
    for i in range(0, 4):
        board.append(sys.stdin.readline().strip())
    sys.stdin.readline().strip()

    for i in range(0, 4):
        r = check_win(board[i])
        if r:
            return r

    for i in range(0, 4):
        l = []
        l.append(board[0][i])
        l.append(board[1][i])
        l.append(board[2][i])
        l.append(board[3][i])
        r = check_win(l)
        if r:
            return r

    l = []
    l.append(board[0][0])
    l.append(board[1][1])
    l.append(board[2][2])
    l.append(board[3][3])
    r = check_win(l)
    if r:
        return r

    l = []
    l.append(board[0][3])
    l.append(board[1][2])
    l.append(board[2][1])
    l.append(board[3][0])
    r = check_win(l)
    if r:
        return r

    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == '.':
                return 'Game has not completed'

    return 'Draw'


num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s " % (case, Solve())
