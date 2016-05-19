import time
from time import sleep
import curses
from curses import KEY_DOWN

curses.initscr()
curses.start_color()
curses.use_default_colors()
screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
screen.box()

score = 0

hisc=open("highscore.txt","w+")
highscore=hisc.read()
highscore_in_no=int(highscore)
if score>highscore_no:
                hisc.write(str(current_score))
                highscore_in_no=current_score

while True:
    select = screen.getch()
    if select == KEY_DOWN:
        screen.refresh()
        score += 1
        print(score)
        with open('score.dat', 'wb') as file:
            pickle.dump(score, file)
    if select == 27:
        screen.refresh()
        break
