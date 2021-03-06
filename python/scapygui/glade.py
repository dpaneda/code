#!/usr/bin/python
import gtk
from gtk import glade
from scapy import *

class Gscapy:
	def __init__(self):
		self.xml = glade.XML("prueba.glade", None, None)
		self.xml.signal_connect("send_b_clicked_cb",self.send)
		self.xml.signal_connect("mainwindow_destroy_cb", gtk.main_quit)
		self.ttl = self.xml.get_widget("ttl_value")
		self.src = self.xml.get_widget("src_value")
		self.dst = self.xml.get_widget("dst_value")

	def send(self, w):
		ttl = int(self.ttl.get_text())
		src = self.src.get_text()
		dst = self.dst.get_text()
		pkg = IP(ttl=ttl,src=src,dst=dst)/ICMP()
		send(pkg)
		print "Sending %s --> %s (ttl %d)" % (src,dst,ttl)

if __name__ == "__main__":
	gscapy = Gscapy()
	gtk.main()
