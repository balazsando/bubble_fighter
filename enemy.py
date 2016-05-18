#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
from time import sleep
import random

screen = curses.initscr()
screen.border(0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

boxes = []

for i in range(5):
    text = "aaa"
    x_pos = random.randrange(1, 74)
    box1 = curses.newwin(3, len(text)+2, 0, x_pos)
    box1.box()
    box1.addstr(1, 1, text)
    screen.refresh()
    box1.refresh()
    sleep(2)
    #box1.mvwin(3,x_pos)

while True:
    event = screen.getch()
    if event == ord('q'): break

curses.endwin()
