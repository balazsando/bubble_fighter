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

def box_move():
    for j in range (1,5):
        for i in boxes:
            box = curses.newwin(3, len(text)+2, 3*j, i[0])
            box.box()
            box.addstr(1, 1, i[1])
            screen.refresh()
            box.refresh()
        sleep(0.2)

for i in range(5):
    text = "aaa"
    x_pos = random.randrange(1, 74)
    box = curses.newwin(3, len(text)+2, 0, x_pos)
    box.box()
    box.addstr(1, 1, text)
    boxes.append([x_pos, text])
    screen.refresh()
    box.refresh()
    sleep(0.2)

box_move()

while True:
    event = screen.getch()
    if event == ord('q'): break

curses.endwin()
