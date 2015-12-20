#!/usr/bin/python2

import sqlite3

sql = sqlite3.connect('users.db')
cursor = sql.cursor()

for id in range(10000, 109999):
    try:
        mod = str(id % 100).zfill(2)
        last_file = "output/last_times/%s/%s.timestamp" % (mod, id)
        feed_file = "output/encrypted/%s/%s.feed" % (mod, id)
        last_time = int(open(last_file).read())
        feed = open(feed_file).read()
        cursor.execute('INSERT INTO users (id, last_time, feed) VALUES (?,?,?)', [id, last_time, buffer(feed)])
        #print("%d (%s) - %d : %s" % (id, mod, last_time, len(feed)))
    except IOError as e:
        print e

cursor.close()
sql.commit()
