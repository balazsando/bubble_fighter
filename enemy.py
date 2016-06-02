#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
from time import sleep
import random
import riddle
import datetime


curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(5, 0, 7)       # DEFINING COLOR FOR BOXES
curses.init_pair(6, 0, 1)       # DEFINING COLOR FOR DESTROYED BOXES BY REACHING END
curses.init_pair(7, 0, 3)       # DEFINING COLOR FOR DESTROYED BOXES BY PLAYER-1
curses.init_pair(8, 0, 4)       # DEFINING COLOR FOR DESTROYED BOXES BY PLAYER-2

curses.noecho()
curses.curs_set(0)

screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
screen.nodelay(1)
screen.timeout(10)

box_content = []        # LIST INCLUDING ALL DATA FOR RIDDLE
multi = 0
score = 0
life = 0
life_2 = 0              # LIFE_2 IS PLAYER 1'S HEALTHBAR IN 2 PLAYER MODE FOR EASIER CODING (RIGHT_TEXT METHOD)


def kill_enemy(color, index=0):
    box = curses.newwin(3, len(box_content[index].text)+2, box_content[index].y_pos, box_content[index].x_pos)
    box.bkgd(curses.color_pair(color))  # VISUALIZATION FOR DESTROYING BOXES
    box.box()
    box.refresh()
    sleep(0.1)
    box_content.pop(index)  # REMOVING BOX'S DATA FROM LIST


def key_pressed(key):
    if key == 27:     # GIVING UP BY PRESSING ESC (OR MANY OTHER FUNCTION KEYS AS IT SEEMS...)
        global life
        global life_2
        life = 0
        life_2 = 0
    elif key != -1:         # IF ANY KEY PRESSED
        for i in range(len(box_content)):
            if multi:                               # 2-PLAYER EVENT
                if box_content[i].input[0] == chr(key):  # PLAYER-1 INPUT
                    life -= 1                         # DAMAGE TO PLAYER-2
                    kill_enemy(7, i)                   # REMOVING BOX FROM SCREEN
                    break
                if box_content[i].input[1] == chr(key):  # PLAYER-2 INPUT
                    life_2 -= 1                      # DAMAGE TO PLAYER-1
                    kill_enemy(8, i)                   # REMOVING BOX FROM SCREEN
                    break
            elif box_content[i].input == chr(key):       # 1-PLAYER EVENT
                global score
                score += 1                        # INCREASING SCORE WHEN RIGHT INPUT GIVEN
                kill_enemy(7, i)                   # REMOVING BOX FROM SCREEN
                break


def box_reach_end():    # BOX REACHING THE GROUND
    box_content.sort(key=lambda box: box.y_pos, reverse=True)
    while ([box for box in box_content if box.y_pos > curses.LINES-7]):
        if not multi:               # 1-PLAYER EVENT (IRRELEVANT IN 2-PLAYER MODE)
            global life
            life -= 1                 # LOSING LIFE
        kill_enemy(6)


def right_text():          # HEADER INFO POSITIONED ON THE RIGHT
    if multi:                   # WHEN IN 2-PLAYER MODE DISPLAYING PLAYER 2 HEALTH BAR
        max_life = 10
        right_text = "P 2: "
    else:                       # WHEN IN 1-PLAYER MODE DISPLAYING PLAYER'S REMAINING LIFE
        max_life = 5
        right_text = "LIFE: "
    for l in range(life):
        right_text += "💚 "
    for l in range(max_life-life):
        right_text += "💀 "
    right_text += str(life)
    return right_text


def left_text():       # HEADER INFO POSITIONED ON THE LEFT
    if multi:               # WHEN IN 2-PLAYER MODE DISPLAYING PLAYER 1 HEALTH BAR
        left_text = "P 1: "
        for l in range(life_2):
            left_text += "💚 "
        for l in range(10-life_2):
            left_text += "💀 "
        left_text += str(life_2)
    else:                   # WHEN IN 1-PLAYER MODE DISPLAYING PLAYER'S SCORE
        left_text = "SCORE: "+str(score)
    return left_text


def header():          # ASSEMBLING ALL INFO IN HEADER
    game_progress = curses.newwin(3, curses.COLS, 0, 0)
    game_progress.box()
    title = "BUBBLE - FIGHTER 1.0"
    game_progress.addstr(1, 1, left_text())
    game_progress.addstr(1, (curses.COLS - len(title)) // 2, title)
    game_progress.addstr(1, curses.COLS-30, right_text())
    game_progress.refresh()


def box_move():            # METHOD FOR MOVING BOXES
    for j in range((multi+2)**2):
        if life == 0 or (multi and life_2 == 0):
            break
        screen.box()
        box_reach_end()
        key_pressed(screen.getch())
        count = 0
        for i in box_content:   # ADDING BOX TO SCREEN
            header()
            i.y_pos += i.speed
            box = curses.newwin(3, len(i.text)+2, i.y_pos, i.x_pos)
            box.attrset(curses.color_pair(5))
            box.addstr(1, 1, i.text)
            box.box()
            box.refresh()
            count += 1
        if box_content:     # IF ALL BOXES DESTROYED CUTS OFF DELAY OF CYCLE
            sleep(0.2)


def box_cloning():         # ADDING BOX DATA TO LIST
    clone = riddle.create_riddle(multi)
    box_content.append(clone)
    box_move()


def solo_start():       # INITIALISING ELEMENTS OF 1-PLAYER MODE
    global multi
    global life
    global score
    global box_content
    multi = 0
    life = 5
    score = 0
    while life > 0:     # CREATING BOXES TILL PLAYER DIES
        box_cloning()
    box_content.clear()
    minute = str(datetime.datetime.now().minute)
    if datetime.datetime.now().minute < 10:
        minute = "0" + str(datetime.datetime.now().minute)
    date = (str(datetime.datetime.now().year)+"."
            + str(datetime.datetime.now().month)+"."
            + str(datetime.datetime.now().day)+"  "
            + str(datetime.datetime.now().hour)+":"
            + minute)
    return [score, date]


def multi_start():      # INITIALISING ELEMENTS OF 2-PLAYER MODE
    global multi
    global life
    global life_2
    multi = 1
    life = 10
    life_2 = 10
    while life > 0 and life_2 > 0:      # CREATING BOXES TILL ONE PLAYER LOSES ALL LIFE
        box_cloning()
    box_content.clear()
    if life == life_2 == 0:             # EVALUATING WHO THE WINNER IS
        return "No one. You have given up :("
    elif life_2 == 0:
        return "P 2"
    else:
        return "P 1"
