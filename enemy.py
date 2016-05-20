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
curses.init_pair(5, 0, 7)       #DEFINING COLOR FOR BOXES

curses.noecho()
curses.curs_set(0)

screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
screen.nodelay(1)
screen.timeout(10)

box_content = []        #LIST INCLUDING ALL DATA FOR RIDDLE
score = 0
life = 0
life_2 = 0              #LIFE_2 IS PLAYER 1'S HEALTHBAR IN 2 PLAYER MODE FOR EASIER CODING (RIGHT_TEXT METHOD)

def kill_enemy(index):
    box_content.pop(index)  #REMOVING BOX'S DATA FROM LIST

def key_pressed(key, multi):
    for i in range(len(box_content)):
        if multi:                               #2-PLAYER EVENT
            global life
            global life_2
            if box_content[i].input[0] == key:  #PLAYER-1 INPUT
                life-=1                         #DAMAGE TO PLAYER-2
                kill_enemy(i)                   #REMOVING BOX FROM SCREEN
                break
            if box_content[i].input[1] == key:  #PLAYER-2 INPUT
                life_2-= 1                      #DAMAGE TO PLAYER-1
                kill_enemy(i)                   #REMOVING BOX FROM SCREEN
                break
        elif box_content[i].input == key:       #1-PLAYER EVENT
            global score
            score+=1                        #INCREASING SCORE WHEN RIGHT INPUT GIVEN
            kill_enemy(i)                   #REMOVING BOX FROM SCREEN
            curses.beep()
            break

def box_reach_end(i, multi):    #BOX REACHING THE GROUND
    if multi == 0:              #1-PLAYER EVENT (IRRELEVANT IN 2-PLAYER MODE)
        global life
        life-=1                 #LOSING LIFE
    kill_enemy(i)

def right_text(multi):          #HEADER INFO POSITIONED ON THE RIGHT
    lifes = ""
    if multi:                   #WHEN IN 2-PLAYER MODE DISPLAYING PLAYER 2 HEALTH BAR
        max_life = 10
        player = "P 2: "
    else:                       #WHEN IN 1-PLAYER MODE DISPLAYING PLAYER'S REMAINING LIFE
        max_life = 5
        player = "LIFE: "
    for l in range(life): lifes += "💚 "
    for l in range(max_life-life): lifes += "💀 "
    lifes += str(life)
    right_text = player+lifes
    return right_text

def left_text(multi):       #HEADER INFO POSITIONED ON THE LEFT
    if multi:               #WHEN IN 2-PLAYER MODE DISPLAYING PLAYER 1 HEALTH BAR
        lifes = ""
        for l in range(life_2): lifes += "💚 "
        for l in range(10-life_2): lifes += "💀 "
        lifes += str(life_2)
        left_text = "P 1: "+lifes
    else:                   #WHEN IN 1-PLAYER MODE DISPLAYING PLAYER'S SCORE
        left_text = "SCORE: "+str(score)
    return left_text

def header(multi):          #ASSEMBLING ALL INFO IN HEADER
    game_progress = curses.newwin(3, curses.COLS, 0, 0)
    game_progress.box()
    title = "BUBBLE - FIGHTER 1.0"
    left = left_text(multi)
    right = right_text(multi)
    game_progress.addstr(1, 1, left)
    game_progress.addstr(1, (curses.COLS - len(title)) //2, title)
    game_progress.addstr(1, curses.COLS-30, right)
    game_progress.refresh()

def box_move(multi):            #METHOD FOR MOVING BOXES
    for j in range ((multi+2)**2):
        screen.border(0)
        event = screen.getch()
        if event != -1:         #IF ANY KEY PRESSED
            if event == 27:
                global life
                life=0
                if multi:
                    global life_2
                    life_2=0
                break
            key_pressed(chr(event), multi)
        count = 0
        for i in box_content:   #ADDING BOX TO SCREEN
            header(multi)
            box = curses.newwin(3, len(i.text)+2, i.y_pos, i.x_pos)
            box.attrset(curses.color_pair(5))
            box.addstr(1, 1, i.text)
            box.box()
            box.refresh()
            if i.y_pos > curses.LINES-5:    #DEFINING WHEN DOES BOX REACH THE GROUND
                box_reach_end(count, multi)
                if life == 0: break         #IF IN 1-PLAYER MODE UPON LOSING ALL LIFE QUIT THE GAME
            i.y_pos += i.speed
            count+=1
        if box_content:     #IF ALL BOXES DESTROYED CUTS OFF DELAY OF CYCLE
            sleep(0.2)

def box_cloning(multi):         #ADDING BOX DATA TO LIST
    clone = riddle.create_riddle(multi)
    box_content.append(clone)
    box_move(multi)

def solo_start():       #INITIALISING ELEMENTS OF 1-PLAYER MODE
    global life
    global score
    global box_content
    life = 5
    score = 0
    while life > 0:     #CREATING BOXES TILL PLAYER DIES
        box_cloning(0)
    box_content.clear()
    return score

def multi_start():      #INITIALISING ELEMENTS OF 2-PLAYER MODE
    global life
    global life_2
    life = 10
    life_2 = 10
    while life > 0 and life_2 > 0:      #CREATING BOXES TILL ONE PLAYER LOSES ALL LIFE
        box_cloning(1)
    box_content.clear()
    if life == 0 and life_2 == 0:       #EVALUATING WHO THE WINNER IS
        return "No one. You have given up :("
    elif life_2 == 0:
        return "P 2"
    else:
        return "P 1"
