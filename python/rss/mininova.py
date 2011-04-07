#!/usr/bin/python
import urllib
import xml.etree.ElementTree as ET # Python 2.5
import os

basedir='.'

class Post(object):
	def __init__(self, item):
		self.link = item.findtext("link")
		self.title = item.findtext("title")
		self.pubdate = item.findtext("pubDate")
		self.category = item.findtext("category")

def getposts(search):
	uri = "http://www.mininova.org/rss/%s" % search
	tree = ET.parse(urllib.urlopen(uri))
	return map(Post, tree.getiterator("item"))

def search(tag):
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

search("prison+break+720p+eztv")
