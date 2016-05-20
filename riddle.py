import random
import string
import curses

class Riddle:
    def __init__(self, text, result, x_pos, y_pos, speed):
        self.text = text        #TEXT DISPLAYED IN BOX
        self.result = result    #INPUT NEEDED TO DESTROY BOX
        self.x_pos = x_pos      #X POSITION IN THE MATRIX
        self.y_pos = y_pos      #Y POSITION IN THE MATRIX
        self.speed = speed      #SPEED OF BOX MOVEMENT

def do_the_math(oper, num1, num2):  #CALCULATING INPUT NEEDED FOR MATH TYPE BOX
    switcher = {
        "+": num1+num2,
        "-": num1-num2,
        "*": num1*num2,
    }
    return switcher.get(oper)

def create_random_arrow():      #CREATING ARROW TYPE BOXES
    arrow = [ "←" , "→", "↑", "↓", "a", "d", "w", "s", "4", "6", "8", "5" ]
    rnd = random.randrange(4)
    new_rid = [arrow[rnd], [arrow[rnd+4], arrow[rnd+8]] ] #CALCULATING DISPLAY AND INPUT NEEDED
    return new_rid


def create_math_problem():      #CREATING MATH TYPE BOXES
    new_result = 10
    while new_result > 9 or new_result < 1: #CALCULATIN MATH TYPE BOXES TILL INPUT NEEDED IS 1-9
        num1 = random.randrange(0,6)
        operation = ['+', '-', '*']
        oper = random.choice(operation)
        num2 = random.randrange(0,6)
        new_text = str(num1)+oper+str(num2)     #CREATING DISPLAY
        new_result = do_the_math(oper, num1, num2)  #CREATING INPUT NEEDED
    new_rid = [new_text, str(new_result)]
    return new_rid


def create_random_letter():     #CREATING LETTER TYPE BOXES
    alphabet = list(string.ascii_lowercase)
    letter = random.choice(alphabet)
    return [letter, letter]     #CREATING DISPLAY+INPUT

def create_riddle(multi):       #CREATING BOX DATA
    if multi:
        riddle = create_random_arrow() #IN 2-PLAYER MODE ONLY ARROW TYPE BOXES
    else:       #IN 1-PLAYER MODE CREATING MATH OR LETTER TYPE BOXES
        type = random.getrandbits(1)
        if type:
            riddle = create_random_letter()
        else:
            riddle = create_math_problem()
    x_pos = random.randrange(5, curses.COLS-5)  #CALCULATING X POSITION FOR BOX
    speed = random.randrange(1,3)       #CALCULATING SPEED FOR BOX
    new_riddle = Riddle(riddle[0], riddle[1], x_pos, 3, speed) #ASSEMBLING BOX DATA
    return new_riddle
