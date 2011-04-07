#!/usr/bin/python
import memcache
from threading import Thread
import time

class memcache_hiter(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)
		self.go = True
		self.hits = 0

	def run(self):
		while self.go:
			self.hits += 1
			self.mc.get("foo")

t = []
count = 0

for i in range(0,9):
	m = memcache_hiter()
	m.start()
	t.append(m)

time.sleep(10)

for i in range(0,9):
	m = t.pop()
	count += m.hits
	m.go = False

print count
print count/10
