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
    for j in range (len(boxes)):
        screen.erase()
        screen.border(0)
        for i in boxes:
            screen.refresh()
            i[1] += i[3]
            box = curses.newwin(3, len(text)+2, i[1], i[0])
            box.box()
            box.addstr(1, 1, i[2])
            box.refresh()
            if i[1] == 20:        #add here LINES coordinate
                print("TT")       #add box reach end
        sleep(0.2)

for i in range(8):
    text = "a"
    x_pos = random.randrange(1, 74)
    speed = random.randrange(1,3)
    box = curses.newwin(3, len(text)+2, 0, x_pos)
    box.box()
    box.addstr(1, 1, text)
    screen.refresh()
    box.refresh()
    boxes.append([x_pos, 0, text, speed])
    box_move()


while True:
    event = screen.getch()
    if event == ord('q'): break

curses.endwin()
