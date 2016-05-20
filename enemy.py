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
curses.init_pair(5, 0, 7)

curses.noecho()
curses.curs_set(0)

screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
screen.nodelay(1)
screen.timeout(10)

box_content = []
score = 0
life = 0
life_2 = 0

def kill_enemy(index):
    box_content.pop(index)

def key_pressed(key, multi):
    for i in range(len(box_content)):
        if multi:
            global life
            global life_2
            if box_content[i].result[0] == key:
                life_2-=1
                kill_enemy(i)
                break
            if box_content[i].result[1] == key:
                life-= 1
                kill_enemy(i)
                break
        else:
            if box_content[i].result == key:
                global score
                score+=1
                kill_enemy(i)
                curses.beep()
                break

def box_reach_end(i, multi):
    if multi == 0:
        global life
        life-=1
    kill_enemy(i)

def right_text(multi):
    lifes = ""
    if multi:
        for l in range(life_2): lifes += "💚 "
        for l in range(10-life_2): lifes += "💀 "
        lifes += str(life_2)
        right_text = "P 2: "+lifes
    else:
        for l in range(life): lifes += "💚 "
        for l in range(5-life): lifes += "💀 "
        lifes += str(life)
        right_text = "LIFE: "+lifes
    return right_text

def left_text(multi):
    if multi:
        lifes = ""
        for l in range(life): lifes += "💚 "
        for l in range(10-life): lifes += "💀 "
        lifes += str(life)
        left_text = "P 1: "+lifes
    else:
        left_text = "SCORE: "+str(score)
    return left_text

def header(multi):
    game_progress = curses.newwin(3, curses.COLS, 0, 0)
    game_progress.box()
    title = "BUBBLE - FIGHTER 1.0"
    left = left_text(multi)
    right = right_text(multi)
    game_progress.addstr(1, 1, left)
    game_progress.addstr(1, (curses.COLS - len(title)) //2, title)
    game_progress.addstr(1, curses.COLS-30, right)
    game_progress.refresh()

def box_move(multi):
    for j in range ((multi+2)**2):
        screen.border(0)
        event = screen.getch()
        if event != -1:
            #if event == 27:
            #    global life
            #    life=0
            #    break
            key_pressed(chr(event), multi)
        count = 0
        for i in box_content:
            header(multi)
            box = curses.newwin(3, len(i.text)+2, i.y_pos, i.x_pos)
            box.attrset(curses.color_pair(5))
            box.addstr(1, 1, i.text)
            box.box()
            box.refresh()
            if i.y_pos > curses.LINES-5:
                box_reach_end(count, multi)
                if life == 0: break
            i.y_pos += i.speed
            count+=1
        if box_content:
            sleep(0.2)

def box_cloning(i):
    clone = riddle.create_riddle(i)
    box_content.append(clone)
    box_move(i)

def solo_start():
    global life
    global score
    global box_content
    life = 5
    score = 0
    while life > 0:
        box_cloning(0)
    box_content.clear()
    return score

def multi_start():
    global life
    global life_2
    life = 10
    life_2 = 10
    while life > 0 and life_2 > 0:
        box_cloning(1)
    box_content.clear()
    if life == 0:
        return "P 2"
    else:
        return "P 1"
