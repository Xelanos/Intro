def greatest(x, y, z):
    """A function that returns the greatest of 3 numbers """
    if x >= y and x >= z:  # check if x is the greatest
        return x
    elif y >= z and y >= x:  # check if y is the greatest
        return y
    else:  # if neither, returns the third which is the greatest
        return z


def smallest(a, b, c):
    """A function that returns the smallest of 3 numbers """
    if a <= b and a <= c:  # check if a is the smallest
        return a
    elif b <= a and b <= c:  # check if b is the smallest
        return b
    else:  # if neither, returns the third which is the smallest
        return c


def largest_and_smallest(num1, num2, num3):
    """ A function that takes 3 numbers and returns
    the greatest one and smallest one
    """
    user_greatest = greatest(num1, num2, num3)
    user_smallest = smallest(num1, num2, num3)
    return user_greatest, user_smallest


