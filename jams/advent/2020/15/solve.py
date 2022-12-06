import sys

l = [20,9,11,0,1,2]
#l = [0,3,6]

turns = {}
for i in range(0, len(l)):
    n = l[i]
    turns[n] = i

last = 0
for i in range(len(l), 30000000 - 1):
    if last not in turns:
        turns[last], last = i, 0
    else:
        turns[last], last = i, i - turns[last]
print(last)
