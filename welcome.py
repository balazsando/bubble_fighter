import curses
import enemy
from curses import KEY_UP, KEY_DOWN
from time import sleep
import os.path
import math
import datetime

curses.initscr()
curses.start_color()
curses.use_default_colors()
screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
game_mode = 0
title = "WELCOME TO RIDDLE FIGHTER 1.0"
welcome = []
welcome.append("        1 - PLAYER        ")
welcome.append("2 - PLAYERS (beta version)")
welcome.append("        HIGH SCORE        ")
gameinf = [[], [], []]
gameinf[0].append("Destroy enemies falling from the sky by solving their riddles!    ")
gameinf[0].append("Solve the math problem or enter the letter to make them disappear.")
gameinf[0].append("      - POINTS are awarded for each enemy killed.                 ")
gameinf[0].append("      - You lose LIFE if enemies reach the ground.                ")
gameinf[1].append("Fight againts another player and prove you have lightning reflexes")
gameinf[1].append("Whoever pressing the correct button first will damage the opponent")
gameinf[1].append("      - LIFE is taken from opponent for each score.               ")
gameinf[1].append("      - P1 use W, A, S, D letters, P2 use 8, 4, 5, 6 numbers      ")
gameinf[2].append("        TOP 3:         SCORE          DATE                        ")
gameinf[2].extend([" "*len(gameinf[2][0])] * 3)
exitinf = "ESC to exit"
gameover = []
gameover.append("Traceback (most recent call last):                  ")
gameover.append("      File \"python/bubble_fighter/welcome.py\", line 20, in <module>")
gameover.append("                                         sdfwefw")
gameover.append("                                 NameError: name 'sdfw")
gameover.append("Just jokin... you got REKT!")
gameover.append("Your score is: ")
gameover.append("NEW HIGH SCORE - CONGRATS")
playerwin = []
playerwin.append("What an intense fight... You both fought well!")
playerwin.append("And the winner is:")
playerwin.append("")
curses.init_pair(1, 1, -1)
curses.init_pair(2, -1, 3)
curses.init_pair(3, -1, 1)
curses.init_pair(4, 7, 0)


def game_menu():
    if game_mode == 2:  # PUTTING TOGETHER HIGHSCORE FOR DISPLAY
        if score_list():
            scores = score_list()
            for i in range(len(scores)):
                if scores:
                    gameinf[2][i+1] = (" "*23 + scores[i][0] + " "*(15-len(scores[i][0])) +
                                       scores[i][1] + " "*(28-len(scores[i][1])))
    screen.addstr(curses.LINES//2-7, (curses.COLS-len(title))//2, title, curses.color_pair(3))
    screen.addstr(curses.LINES-2, curses.COLS-15, exitinf)
    for i in range(len(welcome)):   # DISPLAYING MENU
        screen.addstr(curses.LINES//2+(2*i-5), (curses.COLS-len(welcome[i]))//2, welcome[i],
                      curses.color_pair((game_mode == i)+1))
    for i in range(len(gameinf[game_mode])):    # DISPLAYING GAME MODE INFO
        screen.addstr(curses.LINES//2+(4+i), (curses.COLS-len(gameinf[game_mode][i]))//2, gameinf[game_mode][i],
                      curses.color_pair(4))


def player_win(player):     # END SCREEN FOR 2-PLAYER MODE
    screen.erase()
    playerwin[2] = player
    for i in range(len(playerwin)):
        screen.addstr(curses.LINES//2+2*(i-1), (curses.COLS-len(playerwin[i]))//2, playerwin[i])
        screen.refresh()
        sleep(2)
    screen.erase()


def score_list():
    scores = []
    if os.path.isfile("highscore.csv"):
        with open("highscore.csv") as readfile:
            for line in readfile:
                if line:
                    hs_data = line.rstrip("\n").split(",")
                    scores.append([hs_data[0], hs_data[1]])
    return scores


def exp_score(score):   # UPDATING HIGHSCORE IF PLAYER MAKE IT TO TOP 3
    hs = []
    if score_list():
        hs = score_list()
        if len(hs) < 3:
            hs.append(score)
        else:
            if score[0] > int(hs[2][0]):
                hs.pop(2)
                hs.append(score)
    else:
        hs.append(score)
    hs.sort(key=lambda score: int(score[0]), reverse=True)
    with open("highscore.csv", "w+") as writefile:
        for score in hs:
            writefile.write(str(score[0])+","+score[1]+"\n")


def game_over(score):       # END SCREEN FOR 1-PLAYER MODE
    screen.erase()
    for i in range(4):
        screen.addstr(curses.LINES//3+(i-1), curses.COLS//2, gameover[i])
    screen.refresh()
    sleep(2)
    screen.erase()
    screen.addstr(curses.LINES//2, (curses.COLS-len(gameover[4]))//2, gameover[4])
    screen.refresh()
    sleep(3)
    screen.erase()
    screen.addstr(curses.LINES//2, (curses.COLS-len(gameover[5]))//2, gameover[5]+str(score[0]))
    if score_list():
        if score[0] > int(score_list()[0][0]):
            screen.addstr(curses.LINES//2-2, (curses.COLS-len(gameover[6]))//2, gameover[6])
    else:
        screen.addstr(curses.LINES//2-2, (curses.COLS-len(gameover[6]))//2, gameover[6])
    exp_score(score)
    screen.refresh()
    sleep(3)
    screen.erase()


def welcome_screen():   # GAME MODE SELECTION
    global game_mode
    while True:
        game_menu()     # DISPLAYING MENU SCREEN
        select = screen.getch()
        if select == KEY_DOWN:       # MOVING DOWN IN MENU
            game_mode = (game_mode+1) % 3
        elif select == KEY_UP:      # MOVING UP IN MENU
            game_mode = (game_mode+2) % 3
        elif select == 10 and game_mode < 2:    # STARTING THE GAME
            result = enemy.start_game(game_mode)
            if game_mode == 0:
                game_over(result)
            elif game_mode == 1:
                player_win(result)
        elif select == 27:
            curses.endwin()
            break

welcome_screen()
