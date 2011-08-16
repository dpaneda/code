#!/usr/bin/python
# Dowload wallpaper of the day from national geographic
# TODO would be nice to embed photo captions to know photo background
import urllib,os,re

def download_image(url):
	durl = urllib.urlopen(url)
	if durl.code != 404:
		path = "/tmp/wallpaper.jpg"
		f = open(path, "w")
		f.write(durl.read())
		f.close()
	else:
		print "Not found: " + url

base = "http://photography.nationalgeographic.com/photography/photo-of-the-day"
url = urllib.urlopen(base)
	
for line in url:
    match = re.search("(http://images.nationalgeographic.com/wpf/media-live/photos/.*jpg)\"  width=\"990\"", line)
    if match is not None:
        print "Downloading wallpaper: " + match.group(1)
        download_image(match.group(1))
