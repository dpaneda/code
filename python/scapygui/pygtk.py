#!/usr/bin/python
import gtk

def leave(*args):
	window.hide()
	gtk.main_quit()

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy", leave)
window.set_border_width(10)

windows.__init__(self, 'pygnome-hello-world', 'pygnome_hello')
self.set_wmclass('pygnome_hello', 'pygnome_hello')

box = gtk.VBox(False, 0)
window.add(box)

label = gtk.Label("One tool to rule them all")
ttl = gtk.CheckButton(label="ttl")
src = gtk.CheckButton(label="Source")
dst = gtk.CheckButton(label="Destination")

entry = gtk.Entry()
button = gtk.Button("Aceptar")

for i in (label,ttl,src,dst,entry,button):
	box.add(i)

window.show_all()

gtk.main()
