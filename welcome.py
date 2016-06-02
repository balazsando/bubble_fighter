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
game_mode = 1
welcome1 = "WELCOME TO RIDDLE FIGHTER 1.0"
welcome2 = "        1 - PLAYER        "
welcome3 = "2 - PLAYERS (beta version)"
welcome4 = "        HIGH SCORE        "
soloinf1 = "Destroy enemies falling from the sky by solving their riddles!    "
soloinf2 = "Solve the math problem or enter the letter to make them disappear."
soloinf3 = "      - POINTS are awarded for each enemy killed.                 "
soloinf4 = "      - You lose LIFE if enemies reach the ground.                "
multinf1 = "Fight againts another player and prove you have lightning reflexes"
multinf2 = "Whoever pressing the correct button first will damage the opponent"
multinf3 = "      - LIFE is taken from opponent for each score.               "
multinf4 = "      - P1 use W, A, S, D letters, P2 use 8, 4, 5, 6 numbers      "
highinf1 = "        TOP 3:         SCORE          DATE                        "
exit_inf = "ESC to exit"
gameover1 = "Traceback (most recent call last):                  "
gameover2 = "      File \"python/bubble_fighter/welcome.py\", line 20, in <module>"
gameover3 = "                                         sdfwefw"
gameover4 = "                                 NameError: name 'sdfw"
gameover5 = "Just jokin... you got REKT!"
gameover6 = "Your score is: "
gameover7 = "NEW HIGH SCORE - CONGRATS"
playerwin1 = "What an intense fight... You both fought well!"
playerwin2 = "And the winner is:"
curses.init_pair(1, -1, 1)
curses.init_pair(2, -1, 3)
curses.init_pair(3, 1, -1)
curses.init_pair(4, 7, 0)


def game_mode_1():          # GAME MODE 1 DESCRIPTION - 1 PLAYER
    screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(2))
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome4)) // 2, welcome4, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 + 4, (curses.COLS - len(soloinf1)) // 2, soloinf1, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 5, (curses.COLS - len(soloinf2)) // 2, soloinf2, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 6, (curses.COLS - len(soloinf3)) // 2, soloinf3, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 7, (curses.COLS - len(soloinf4)) // 2, soloinf4, curses.color_pair(4))
    global game_mode
    game_mode = 1


def game_mode_2():          # GAME MODE 2 DESCRIPTION - 2 PLAYERS
    screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(2))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome4)) // 2, welcome4, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 + 4, (curses.COLS - len(multinf1)) // 2, multinf1, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 5, (curses.COLS - len(multinf2)) // 2, multinf2, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 6, (curses.COLS - len(multinf3)) // 2, multinf3, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 7, (curses.COLS - len(multinf4)) // 2, multinf4, curses.color_pair(4))
    global game_mode
    game_mode = 2


def high_score():
    screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome4)) // 2, welcome4, curses.color_pair(2))
    scores_format = [" " * len(highinf1), " " * len(highinf1), " " * len(highinf1)]
    if score_list():
        scores = score_list()
        for i in range(len(scores)):
            scores_format[i] = str(" " * 23 + scores[i][0]
                                   + " " * (15 - len(scores[i][0])) + scores[i][1] + " " * (28 - len(scores[i][1])))
    screen.addstr(curses.LINES // 2 + 4, (curses.COLS - len(highinf1)) // 2, highinf1, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 5, (curses.COLS - len(highinf1)) // 2, scores_format[0], curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 6, (curses.COLS - len(highinf1)) // 2, scores_format[1], curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 7, (curses.COLS - len(highinf1)) // 2, scores_format[2], curses.color_pair(4))
    global game_mode
    game_mode = 3


def player_win(player):     # END SCREEN FOR 2-PLAYER MODE
    screen.erase()
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(playerwin1)) // 2, playerwin1)
    screen.refresh()
    sleep(2)
    screen.addstr(curses.LINES // 2, (curses.COLS - len(playerwin2)) // 2, playerwin2)
    screen.refresh()
    sleep(1)
    screen.addstr(curses.LINES // 2+2, (curses.COLS - len(player)) // 2, player)
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


def exp_score(score):
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
    screen.addstr(curses.LINES // 3 - 1, curses.COLS // 2, gameover1)
    screen.addstr(curses.LINES // 3, curses.COLS // 2, gameover2)
    screen.addstr(curses.LINES // 3 + 1, curses.COLS // 2, gameover3)
    screen.addstr(curses.LINES // 3 + 2, curses.COLS // 2, gameover4)
    screen.refresh()
    sleep(2)
    screen.erase()
    screen.addstr(curses.LINES // 2, (curses.COLS - len(gameover5)) // 2, gameover5)
    screen.refresh()
    sleep(3)
    screen.erase()
    screen.addstr(curses.LINES // 2, (curses.COLS - len(gameover6)) // 2, gameover6+str(score[0]))
    if score[0] > int(score_list()[0][0]):
        screen.addstr(curses.LINES // 2 - 2, (curses.COLS - len(gameover7)) // 2, gameover7)
    exp_score(score)
    screen.refresh()
    sleep(3)
    screen.erase()


def game_info():        # IN-GAME MENU (GAME NAME, EXIT INFO)
    screen.addstr(curses.LINES // 2 - 7, (curses.COLS - len(welcome1)) // 2, welcome1, curses.color_pair(1))
    screen.addstr(curses.LINES - 2, curses.COLS - 15, exit_inf)


def welcome_screen():   # GAME MODE SELECTION
    game_mode_1()       # 1-PLAYER MODE DEFAULT UPON LAUNCHING GAME
    while True:
        game_info()
        select = screen.getch()
        if game_mode == 1 and select == KEY_DOWN:
            game_mode_2()
        elif game_mode == 2:
            if select == KEY_UP:
                game_mode_1()
            elif select == KEY_DOWN:
                high_score()
        elif game_mode == 3 and select == KEY_UP:
            game_mode_2()
        if select == 10:
            if game_mode == 1:
                score = enemy.solo_start()
                game_over(score)
                game_mode_1()
            elif game_mode == 2:
                player = enemy.multi_start()
                player_win(player)
                game_mode_2()
        elif select == 27:
            curses.endwin()
            break

welcome_screen()
