import pygtk
import gtk

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy", gtk.main_quit)

box = gtk.VBox(False, 0)
window.add(box)

label = gtk.Label("Hola Mundo")
c1 = gtk.CheckButton(label="Uno")
c2 = gtk.CheckButton(label="Dos")
entry = gtk.Entry()
button = gtk.Button("Aceptar")

box.add(label)
box.add(c1)
box.add(c2)
box.add(entry)
box.add(button)

window.show_all()

gtk.main()
