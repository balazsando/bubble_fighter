#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses

screen = curses.initscr()
screen.border(0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

text = "This is a Sample Curses Script"
box1 = curses.newwin(10, len(text)+2, 0, 0)
box1.box()


screen.refresh()
box1.refresh()
box1.addstr(1, 1, text)
box1.refresh()

while True:
   event = screen.getch()
   if event == ord("q"): break

curses.endwin()
