#!/usr/bin/python2

import sys
import math

def impact(vel, pos, room):
  if pos[0] == math.floor(pos[0]) and  pos[0] == math.floor(pos[0]):
    print "fuck! a corner"
    return vel

  vel[0] = - vel[0]
  vel[1] = - vel[1]
  return vel

def check_reflection(vel, pos, room, D):
  while D > 0:
    pos[0] += vel[0]
    pos[1] += vel[1]
    x = int(math.floor(pos[0]))
    y = int(math.floor(pos[1]))

    print pos[1], pos[0]

    if room[y][x] == 'X':
      if (pos[0] - x) == 0.5 and pos[1] - y == 0.5:
        return True
    elif room[y][x] == '#':
      vel = impact(vel, pos, room)

  return False

def Solve():
  [h, w, D] = map(int, sys.stdin.readline().split())

  room = []
  for i in xrange(0, h):
    room.append(sys.stdin.readline().strip())
  
  print h
  print w
  print D
  for i in room:
    print i

  pos = [0, 0]
  vel = [0.2, -1]

  for i in xrange(0, h):
    for j in xrange(0, w):
      if (room[j][i] == 'X'):
        pos = [i + 0.5, j + 0.5]

  print pos
  print vel

  refs = 0
  refs += check_reflection(vel, pos, room, D)

  return refs

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, Solve())
