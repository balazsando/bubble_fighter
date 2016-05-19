import random
import string
import curses

class Riddle:
    def __init__(self, text, result, x_pos, y_pos, speed):
        self.text = text
        self.result = result
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed

def do_the_math(oper, num1, num2):
    switcher = {
        "+": num1+num2,
        "-": num1-num2,
        "*": num1*num2,
    }
    return switcher.get(oper)


def create_math_problem():
    new_result = 10
    while new_result > 9 or new_result < 0:
        num1 = random.randrange(0,6)
        operation = ['+', '-', '*']
        oper = random.choice(operation)
        num2 = random.randrange(0,6)
        new_text = str(num1)+oper+str(num2)
        new_result = do_the_math(oper, num1, num2)
    new_rid = [new_text, str(new_result)]
    return new_rid


def create_random_letter():
    alphabet = list(string.ascii_lowercase)
    letter = random.choice(alphabet)
    return [letter, letter]

def create_riddle():
    type = random.getrandbits(1)
    if type:
        riddle = create_random_letter()
    else:
        riddle = create_math_problem()
    x_pos = random.randrange(5, curses.COLS-5)
    speed = random.randrange(1,3)
    new_riddle = Riddle(riddle[0], riddle[1], x_pos, 3, speed)
    return new_riddle
