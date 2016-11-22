import math


def circle_area(radius):
    """Takes the radius of a circle and returns it's area"""
    radius_squared = math.pow(radius, 2)
    circ_area = radius_squared * math.pi  # pi times radius squared

    return circ_area


def rectangle_area(first_leg, second_leg):
    """Takes two legs  and returns rectangle area"""
    rec_area = first_leg * second_leg

    return rec_area


def trapoziod_area(first_base, second_base, hight):
    """Takes two bases and height and returns trapezoid area"""
    trap_area = ((first_base + second_base) / 2) * hight

    return trap_area


def shape_area():
    """A function that calculates the area of shapes
    based on the user's input.
    user has to input required shape and shape parameters"""

    shape_number = int(input("Choose shape "
                             "(1=circle, 2=rectangle, 3=trapezoid): "))

    if shape_number == 1:
        # waits for radius input and returns circle area
        rad = float(input())

        return circle_area(rad)

    elif shape_number == 2:
        # waits for two legs input and returns rectangle area
        leg_1 = float(input())
        leg_2 = float(input())

        return rectangle_area(leg_1, leg_2)

    elif shape_number == 3:
        # waits for two bases and height input and returns trapezoid area
        base_1 = float(input())
        base_2 = float(input())
        h = float(input())

        return trapoziod_area(base_1, base_2, h)

    else:
        return None

