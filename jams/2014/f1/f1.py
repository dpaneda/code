#!/usr/bin/python
import curses
import os

def initcurses(scr):
	curses.noecho()
	curses.cbreak()
	scr.keypad(1)

def endcurses(scr):
	curses.nocbreak();
	scr.keypad(0);
	curses.echo()
	curses.endwin()

def main(main_win):
	c = cursor = selected = entries = 0
	actual_dir = os.getcwd()


	initcurses(main_win)
	main_win.border(0)
	main_win.refresh()

	(ymax, xmax) = list(main_win.getmaxyx())

	tup = [0, 0, 4, 3, ymax - 3, xmax - 3]
	win = curses.newpad(1000, xmax)

	initcurses(win)
	#curses.curs_set(2)

	while True:
		y,x = 0, 0
		edirs, efiles = [], []
		main_win.clear()
		#main_win.addstr(ymax - 1, 2, "Key: %s (%d)\t\t Cursor: %d\t Selected: %d\t Entries: %d"
		#				% (curses.keyname(c), c, cursor, selected, entries))
		main_win.addstr(ymax - 1, 2, "Cursor: %d - %d" % win.getyx())
		main_win.addstr(2, 3, "Directorio actual: " + actual_dir, curses.A_BOLD)

		win.addstr(y, x, "..", curses.A_NORMAL)
		y += 1

		for root, dirs, files in os.walk(actual_dir, topdown=True):
			for dir in dirs:
				win.addstr(y, x, dir + '/', curses.A_NORMAL)
				edirs.append(dir)
				y += 1

			del dirs[:]

			for file in files:
				win.addstr(y, x, file, curses.A_NORMAL)
				efiles.append(file)
				y += 1

		entries = len(edirs) + len(efiles) + 1

		#win.chgat(cursor, x, -1, curses.A_STANDOUT)
		win.chgat(selected, x, -1, curses.A_BOLD)

		main_win.refresh()
		win.refresh( *tup )

		c = win.getch()
		if c == curses.KEY_UP and cursor > 0:
			(cy, cx) = win.getyx()
			win.move(cy - 1, cx)
			#cursor -= 1
			#if cursor < tup[0]:
			#	tup[0] -= 1
		if c == curses.KEY_DOWN and cursor < entries:
			(cy, cx) = win.getyx()
			win.move(cy + 1, cx)
			#cursor += 1
			#if cursor > tup[4] + tup[0]:
			#	tup[0] += 1
		if c == 10:
			if cursor == 0:
				actual_dir = os.path.normpath(actual_dir + '/..')
			elif cursor <= len(edirs):
				actual_dir = os.path.normpath(actual_dir + '/' + edirs[cursor - 4])
		if c == ord('q') or c == ord('Q') or c == 27:
			break
		main_win.refresh()
		win.refresh( *tup )

	endcurses(win)

curses.wrapper(main)
