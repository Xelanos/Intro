##############################################
# FILE: math_print.py
# WRITER: Or Mizrahi, Xelanos, 308484625
# DESCRIPTION: some math calculations printed
##############################################

import math


def golden_ratio():
    """ prints the golden ratio using it's Algebraic form """

    print((1 + math.sqrt(5)) / 2)



def square_five():
    """ prints 5 squared """
    print(math.pow(5, 2))


def hypotenuse():
    """ prints hypotenuse of a right-angled triangle """
    LEG1 = 4
    LEG2 = 5
    hypotenuse_squared = math.pow(LEG1, 2) + math.pow(LEG2, 2)
    print(math.sqrt(hypotenuse_squared))


def pi():
    """ prints pi """
    print(math.pi)


def e():
    """ prints e """
    print(math.e)


def squares_area():
    """ prints the area of squares"""
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2),
          math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2),
          math.pow(10, 2))
