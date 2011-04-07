#!/usr/bin/python

import urllib
import os

basedir='.'

def get_jpg(url):
	retcode = call("wget -r -l1 --no-parent -A.jpg " + url)
    if retcode < 0:
		print >>sys.stderr, "Child was terminated by signal", -retcode
		return -1
	
	for post in getposts(tag):
		targetfile = "%s/%s/%s.torrent" % (basedir,tag,os.path.basename(post.link))
		if os.path.exists(targetfile):
			return
		print "Downloading " + post.title, post.link
		url = urllib.urlopen(post.link)
		targetdir = "%s/%s" % (basedir,tag)
		if not os.path.exists(targetdir):
			os.mkdir(targetdir)
		f = open(targetfile,'w')
		f.write(url.read())
		f.close()

search("")
