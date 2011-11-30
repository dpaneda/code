#!/usr/bin/python2
# Dowload wallpaper of the day from national geographic
import urllib,os,re
import Image, ImageDraw, ImageFont

WALLPAPER = "/tmp/wallpaper.jpg"

def download_image(url):
	durl = urllib.urlopen(url)
	if durl.code != 404:
		f = open(WALLPAPER, "w")
		f.write(durl.read())
		f.close()
	else:
		print "Not found: " + url

base = "http://photography.nationalgeographic.com/photography/photo-of-the-day"
url = urllib.urlopen(base)
caption = "Fail"

for line in url:
    match = re.search("(http://images.nationalgeographic.com/wpf/media-live/photos/.*jpg)\"  width=\"990\"", line)
    if match is not None:
        print "Downloading wallpaper: " + match.group(1)
        download_image(match.group(1))
    match = re.search("<h1>(.*)</h1>", line)
    if match is not None:
        caption = match.group(1)

font = ImageFont.truetype("/home/daniel/shared/fonts/LiberationMono-Bold.ttf",40)
img = Image.open(WALLPAPER)
img.resize((1680, 1050))
draw = ImageDraw.Draw(img)
pos = (img.size[0] / 4, img.size[1] - 80)
draw.text(pos, caption, "Yellow", font=font)

img.save(WALLPAPER)
