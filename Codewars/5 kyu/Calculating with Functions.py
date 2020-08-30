def zero(*args):
    num='0'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def one(*args):
    num='1'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def two(*args):
    num='2'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def three(*args):
    num='3'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def four(*args):
    num='4'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def five(*args):
    num='5'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def six(*args):
    num='6'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def seven(*args):
    num='7'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def eight(*args):
    num='8'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)

def nine(*args):
    num='9'
    string=''
    if len(args) > 0:
        eq=str(args[0])
        for i in args:
            string+=str(i)
        equation=num+eq
        return int(eval(equation))
    else:
        return int(num)


def plus(num):
    return '+'+str(num)
def minus(num):
    return '-'+str(num)
def times(num):
    return '*'+str(num)
def divided_by(num):
    return '/'+str(num)























'''This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))'''
