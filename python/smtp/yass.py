#!/usr/bin/python

import smtplib
import time
import threading

class Worker(threading.Thread):
	sended = 0
	def run(self):
		self.show_rate()
		server = smtplib.SMTP("localhost",25000)
		while True:
			server.sendmail("dpaneda@gmail.com", "pala@g.com", "esto es un mensajazo")
			self.sended += 1
	def show_rate(self):
		print self.sended
		self.sended = 0
		t = threading.Timer(1,self.show_rate)
		t.start()

worker = Worker()
worker2 = Worker()
worker3 = Worker()
worker4 = Worker()

worker.start()
worker2.start()
#worker3.start()
#worker4.start()
