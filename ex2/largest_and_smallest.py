def greatest(x, y, z):
    """A function that returns the greatest of 3 numbers """
    if x >= y and x >= z:  # check if x is the greatest
        return x
    elif y >= z and y >= x:  # check if y is the greatest
        return y
    else:  # if neither, returns the third
        return z


def smallest(a, b, c):
    """A function that returns the smallest of 3 numbers """
    if a <= b and a <= c:  # check if a is the smallest
        return a
    elif b <= a and b <= c:  # check if b is the smallest
        return b
    else:  # if neither, returns the third
        return c


def largest_and_smallest(num1, num2, num3):
    """ A function that takes 3 numbers and returns
    the greatest one and smallest one
    """
    GREATEST = greatest(num1, num2, num3)
    SMALLEST = smallest(num1, num2, num3)
    return GREATEST, SMALLEST


