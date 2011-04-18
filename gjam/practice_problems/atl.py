#!/usr/bin/python

import sys

class Maze:
	def __init__(self):
		self.facing_strings = ("N", "E", "S", "W")
		self.open_mask = (0x1, 0x8, 0x2, 0x4)

		self.facing = 2
		self.maze = {}
		self.position = [0, 0]
		self.cornerup = [0, 0]
		self.cornerdown = [0, 0]

	def UpdateMask(self):
		strpos = str(self.position)
		if not self.maze.has_key(strpos):
			self.maze[strpos] = 0
		self.maze[str(self.position)] |= self.open_mask[self.facing]

	def Adjust(self):
		self.facing = self.facing % 4

	def RotateRight(self):
		self.facing += 1
		self.Adjust()

	def RotateLeft(self):
		self.facing -= 1
		self.Adjust()

	def Turn(self):
		self.facing += 2
		self.Adjust()

	def __str__(self):
		cad = "Maze Status:\nFacing\n" + str(self.facing_strings[self.facing]) 
		cad += "\nPosition\n" + str(self.position) 
		cad += "\nMaze\n" + str(self.maze) 
		cad += "\nCornerUp\n" + str(self.cornerup)
		cad += "\nCornerDown\n" + str(self.cornerdown)
		return cad

	def DumpMaze(self):
		for y in range(self.cornerup[1], self.cornerdown[1] + 1):
			line = ""
			for x in range(self.cornerup[0], self.cornerdown[0] + 1):
				index = [x, y]
				line += "%x" % self.maze[str(index)]
			print line
				
	def Walk(self):
		self.UpdateMask()

		if self.facing == 0:
			self.position[1] -= 1
		elif self.facing == 2:
			self.position[1] += 1
		elif self.facing == 1:
			self.position[0] += 1
		elif self.facing == 3:
			self.position[0] -= 1

		self.LimitsAdjust()

	def LimitsAdjust(self):
		if self.position[0] < self.cornerup[0]:
			self.cornerup[0] = self.position[0]
		if self.position[1] < self.cornerup[1]:
			self.cornerup[1] = self.position[1]
		if self.position[0] > self.cornerdown[0]:
			self.cornerdown[0] = self.position[0]
		if self.position[1] > self.cornerdown[1]:
			self.cornerdown[1] = self.position[1]

	def Process(self, direction):
		if direction == 'R':
			self.RotateRight()
		elif direction == 'L':
			self.RotateLeft()
		elif direction == 'W':
			self.Walk()
		
num = int(sys.stdin.readline())

for i in range(1, num+1):
	line = sys.stdin.readline().split()
	fw = line[0][1:-1]
	bw = line[1][1:-1]
	maze = Maze()
	for d in fw:
		maze.Process(d)
	maze.UpdateMask()
	maze.Turn()
	for d in bw:
		maze.Process(d)
	maze.UpdateMask()
	print "Case #%d:" % i
	maze.DumpMaze()
