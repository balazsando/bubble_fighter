import random
import string

class Riddle:
    def __init__(self, text, result):
        self.text = text
        self.result = result

def do_the_math(oper, num1, num2):
    switcher = {
        "+": num1+num2,
        "-": num1-num2,
        "*": num1*num2,
        "/": num1//num2
    }
    return switcher.get(oper)


def create_math_problem():
    num1 = random.randrange(0,21)
    operation = ['+', '-', '*', '/']
    oper = random.choice(operation)
    num2 = random.randrange(1,21)
    new_text = str(num1)+oper+str(num2)
    new_result = do_the_math(oper, num1, num2)
    newrid = Riddle(new_text, new_result)
    return newrid


def create_random_key():
    sleep(1)

def create_random_special_key():
    sleep(1)


x=create_math_problem()
print(str(x.text)+" "+str(x.result))
