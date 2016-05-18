import curses

def main(startscr):
    field = curses.newwin(5, 5, 0, 0)

    game_over = 'Game Over!'
    win.addstr(curses.LINES // 2, (curses.COLS - len(game_over)) // 2, game_over)

curses.wrapper(main)
