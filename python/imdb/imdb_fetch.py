#!/usr/bin/python
import imdb
import sys
from pprint import pprint

ia = imdb.IMDb('mobile')
lista = sys.stdin.readlines()

director = {}

for name in lista:
	try:
		movie = ia.search_movie(name,results=1)[0]
		ia.update(movie)
		d_name = str(movie["director"][0])
		
		if not director.has_key(d_name):
			director[d_name] = {}
		director[d_name][movie["title"]] = movie
		print "%f: %s" % (movie["rating"], movie["title"])
	except:
		continue

for (d_name,d_movies) in director.items():
	print d_name
	for (m_name, m) in d_movies.items():
		print "\t %s: %f" % (m["title"], m["rating"])

for (d_name,d_movies) in director.items():
	for (m_name, m) in d_movies.items():
		print "%f: %s" % (m["rating"], m["title"])

