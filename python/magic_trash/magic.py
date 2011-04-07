#!/usr/bin/python
from pynotify import *
from subprocess import *
import sys

def notify(message=""):
	n = Notification("Packages to remove: ", message)
	n.show()

init("Magic Trash notify")

if not len(sys.argv) > 1:
	sys.exit(1)

file = sys.argv[1]

output = Popen(["dpkg", "-S", file], stdout=PIPE).communicate()[0]
pkg_list = output.split(":")[0]

pkgs = pkg_list.split(",")

notify(pkg_list)



