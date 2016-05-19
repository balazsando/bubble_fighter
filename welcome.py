import curses
import time
from time import sleep
from curses import COLOR_RED
from curses import KEY_UP, KEY_DOWN, KEY_ENTER

screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
screen.border(0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)


def welcome_screen():
    welcome1 = "WELCOME TO RIDDLE FIGHTER 1.0"
    welcome2 = "       1 - PLAYER        "
    welcome3 = "2 - PLAYERS (coming soon)"
    welcome4 = "Destroy enemies falling from the sky by solving their riddles!    "
    welcome5 = "Solve the math problem or enter the letter to make them disappear."
    welcome6 = "      - POINTS are awarded for each enemy killed.                 "
    welcome7 = "      - You lose LIFE if enemies reach the ground.                "
    game_mode = 1
    curses.init_pair(1,-1,1)
    curses.init_pair(2,-1,3)
    curses.init_pair(3,1,-1)
    curses.init_pair(4,7,0)
    screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome1)) // 2, welcome1, curses.color_pair(1))
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(2))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 + 4, (curses.COLS - len(welcome4)) // 2, welcome4, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 5, (curses.COLS - len(welcome5)) // 2, welcome5, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 6, (curses.COLS - len(welcome6)) // 2, welcome6, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 7, (curses.COLS - len(welcome7)) // 2, welcome7, curses.color_pair(4))
    while True:
        event = screen.getch()
        if event == KEY_DOWN and game_mode == 1:
            screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(3))
            screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(2))
            game_mode = 2
            screen.refresh()
        if event == KEY_UP and game_mode == 2:
            screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(2))
            screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(3))
            game_mode = 1
            screen.refresh()
        if event == 10 and game_mode == 1:
            screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome1)) // 2, welcome1, curses.color_pair(2))
            break


welcome_screen()
curses.endwin()
