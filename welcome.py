import curses
import enemy
from curses import KEY_UP, KEY_DOWN
from time import sleep

curses.initscr()
curses.start_color()
curses.use_default_colors()
screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
game_mode = 1
welcome1 = "WELCOME TO RIDDLE FIGHTER 1.0"
welcome2 = "       1 - PLAYER        "
welcome3 = "2 - PLAYERS (coming soon)"
welcome4 = "Destroy enemies falling from the sky by solving their riddles!    "
welcome5 = "Solve the math problem or enter the letter to make them disappear."
welcome6 = "      - POINTS are awarded for each enemy killed.                 "
welcome7 = "      - You lose LIFE if enemies reach the ground.                "
exit_inf = "ESC to exit"
gameover1 = "Traceback (most recent call last):                  "
gameover2 = "      File \"python/bubble_fighter/welcome.py\", line 20, in <module>"
gameover3 = "                                         sdfwefw"
gameover4 = "                                 NameError: name 'sdfw"
gameover5 = "Just jokin... you got REKT!"
curses.init_pair(1,-1,1)
curses.init_pair(2,-1,3)
curses.init_pair(3,1,-1)
curses.init_pair(4,7,0)

def game_mode_1():
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(2))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(3))
    global game_mode
    game_mode = 1

def game_mode_2():
    screen.addstr(curses.LINES // 2 - 3, (curses.COLS - len(welcome2)) // 2, welcome2, curses.color_pair(3))
    screen.addstr(curses.LINES // 2 - 1, (curses.COLS - len(welcome3)) // 2, welcome3, curses.color_pair(2))
    global game_mode
    game_mode = 2

def game_over():
    screen.erase()
    screen.addstr(curses.LINES // 3 - 1, curses.COLS // 2, gameover1)
    screen.addstr(curses.LINES // 3, curses.COLS // 2, gameover2)
    screen.addstr(curses.LINES // 3 + 1, curses.COLS // 2, gameover3)
    screen.addstr(curses.LINES // 3 + 2, curses.COLS // 2, gameover4)
    screen.refresh()
    sleep(2)
    screen.erase()
    screen.addstr(curses.LINES // 2, (curses.COLS -len(gameover5)) // 2, gameover5)
    screen.refresh()
    sleep(3)
    screen.erase()
    screen.addstr(curses.LINES // 2, (curses.COLS - 1) // 2, "nub")
    screen.refresh()
    sleep(1)
    screen.erase()

def game_info():
    screen.addstr(curses.LINES // 2 - 5, (curses.COLS - len(welcome1)) // 2, welcome1, curses.color_pair(1))
    screen.addstr(curses.LINES // 2 + 4, (curses.COLS - len(welcome4)) // 2, welcome4, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 5, (curses.COLS - len(welcome5)) // 2, welcome5, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 6, (curses.COLS - len(welcome6)) // 2, welcome6, curses.color_pair(4))
    screen.addstr(curses.LINES // 2 + 7, (curses.COLS - len(welcome7)) // 2, welcome7, curses.color_pair(4))
    screen.addstr(curses.LINES - 2, curses.COLS - 15, exit_inf)

def welcome_screen():
    game_mode_1()
    while True:
        game_info()
        select = screen.getch()
        if select == KEY_DOWN:
            game_mode_2()
        if select == KEY_UP:
            game_mode_1()
        if select == 10 and game_mode == 1:
            enemy.game_start()
            game_over()
            game_mode_1()
        if select == 27:
            curses.endwin()
            break

welcome_screen()
