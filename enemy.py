#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
from time import sleep
import random
import riddle


curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, 0, 7)

curses.noecho()
curses.curs_set(0)

screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
screen.timeout(10)

box_content = []
score = 0
life = 5

def kill_enemy(index):
    box_content.pop(index)

def key_pressed(key):
    for i in range(len(box_content)-1):
        if box_content[i].result == key:
            global score
            score+=1
            kill_enemy(i)
            break

def box_reach_end(i):
    global life
    life-=1
    kill_enemy(i)

def box_move():
    for j in range (5):
        screen.border(0)
        event = screen.getch()
        if event != -1:
            key_pressed(chr(event))
        count = 0
        for i in box_content:
            game_progress = curses.newwin(3, curses.COLS, 0, 0)
            game_progress.box()
            game_progress.addstr(1, 1, "SCORE: "+str(score))
            lifes = ""
            for l in range(life):
                lifes += "💚 "
            for l in range(5-life):
                lifes += "💀 "
            lifes += str(life)
            life_text = "LIFE: "+lifes
            game_progress.addstr(1, curses.COLS-20, life_text)
            game_progress.refresh()
            box = curses.newwin(3, len(i.text)+2, i.y_pos, i.x_pos)
            box.attrset(curses.color_pair(1))
            box.addstr(1, 1, i.text)
            box.box()
            box.refresh()
            screen.refresh()
            if i.y_pos > curses.LINES-5:        #add here LINES coordinate
                box_reach_end(count)
            i.y_pos += i.speed
            count+=1
        sleep(0.2)



while life > 0:
    clone = riddle.create_riddle()
    box_content.append(clone)
    box_move()

curses.endwin()
