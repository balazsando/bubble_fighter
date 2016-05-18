#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
from time import sleep

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

for i in range(10) :
    box1 = curses.newwin(10, len(text)+2, i, i)
    box1.border(0)
    box1.addstr(1, 1, str(i))
    box1.refresh()
    screen.refresh()
    sleep(1)

while True:
    event = screen.getch()
    if event == ord('q'): break

curses.endwin()
