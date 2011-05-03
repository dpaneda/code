#!/usr/bin/python
import sys

def debug_print(outstr):
    return
    print outstr     

class Table:
    pos = {}
    i,j,r,b,dim,n = 0,0,0,0,0,0
    red = False
    blue = False

    def __init__(self, dim, n):
        self.dim = dim
        self.n = n

    def reset_pos(self):
        self.i,self.j = 0,0

    def reset_counters(self):
        self.r,self.b = 0,0
    
    def current(self):
        return self.pos[self.i][self.j]
    
    def current_line(self):
        return self.pos[self.i]

    def out_limits(self):
        try:
            self.pos[self.i][self.j]
            return False
        except:
            return True

    def move_diag_ur(self):
        self.i -= 1
        self.j += 1

    def move_diag_ul(self):
        self.i -= 1
        self.j -= 1

    def move_diag_dl(self):
        self.i += 1
        self.j -= 1

    def move_diag_dr(self):
        self.i += 1
        self.j += 1

    def update_winners(self):
        if self.r >= table.n:
            self.red = True
        if self.b >= table.n:
            self.blue = True

    def update_counters(self):
        if self.pos[self.i][self.j] == 'B':
            self.b += 1
            self.r = 0
        elif self.pos[self.i][self.j] == 'R':
            self.b = 0
            self.r += 1
        else:
            self.r = self.b = 0

    def check_until_out(self, movement):
        debug_print("Diag moving out!")
        is_out = False
        self.reset_counters()
        while not self.out_limits():
            debug_print(str(self))
            self.update_counters()
            self.update_winners()
            movement()
    
    def walk_diag(self):
        for i in range(0, dim):
            self.i, self.j = i, 0
            self.check_until_out(table.move_diag_dr)
            self.i, self.j = i, 0
            self.check_until_out(table.move_diag_ur)
        
        for i in range(0, dim):
            self.i, self.j = i, table.dim - 1
            self.check_until_out(table.move_diag_dl)
            self.i, self.j = i, table.dim - 1
            self.check_until_out(table.move_diag_ul)
    
    def check_horiz(self):
        self.reset_counters()
        for self.i in range(0, self.dim):
            self.update_counters()
            self.update_winners()

    def __str__(self):
        tmp = self.pos[self.i]
        if not self.out_limits():
            l = list(self.pos[self.i])
            l[self.j] = 'X'
            self.pos[self.i] = "".join(l)
        out = ""
        for x in range(0, dim):
            out += self.pos[x] + "\n"
        self.pos[self.i] = tmp
        out += "Red %d - Blue %d\n" % (self.red, self.blue)
        return out

num = int(sys.stdin.readline())


for case in range(1, num+1):
    dim, n = map(int, sys.stdin.readline().split())
    table = Table(dim,n)
    for i in range(0, dim):
        line = sys.stdin.readline()
        # This translate simulate the gravity action
        line = line.translate(None,"\n.")
        # [::-1] reverses the string, to simulate gravity to the right
        line = line[::-1]
        # Padding to create a dictionary who behaviours like a matrix
        line = line.ljust(dim,'.')
        table.pos[i] = line

    debug_print("%d %d" % (dim, n))
    debug_print(str(table))

    # This code is truncated because the file was accidentally deleted, and this is
    # all I can recover scanning the disk. Maybe sometime i re-implement the missing code
