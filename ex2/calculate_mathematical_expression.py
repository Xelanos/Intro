def subtract(num1, num2):
    """ return the remainder of
    subtracting the 2nd number inputted from the first
    """
    return num1 - num2


def add(num1, num2):
    """ return the addition of the two inputted numbers """
    return num1 + num2


def divide(num1, num2):
    """ return the quotient between the two numbers
     when num1 is the dividend, and num2 the divisor
     CANNOT DIVIDE BY 0!!!!
      """
    if num2 == 0:
        return None  # only ruth lawrance is allowed to dived by 0
    else:
        quotient = num1 / num2
        return float(quotient)


def multiply(num1, num2):
    """ returns the product of two inputted numbers  """
    return num1 * num2


def calculate_mathematical_expression(NUMBER1, NUMBER2, OPERATOR):
    """ Takes two numbers (int or float) and one of the basic
    4 operators  {'+','-','*','/'} as a string and returns
     the result of using the operator with the numbers provided.
     """
    if OPERATOR == '+':
        return add(NUMBER1, NUMBER2)

    elif OPERATOR == '*':
        return multiply(NUMBER1, NUMBER2)

    elif OPERATOR == '-':
        return subtract(NUMBER1, NUMBER2)

    elif OPERATOR == '/':
        return divide(NUMBER1, NUMBER2)
    else:
        return None

def calculate_from_string(math_string):
    """ Take a string in the format of :
    NUMBER-space-OPERATOR-space-NUMBER
    and does the calculation written
    in the string.
    (calculation from left to right,
    as normal)/
    """
    seprated_math_string=math_string.split(None,) #spiltting the stirng

    # extracting the numbers and operator
    first_number=float(seprated_math_string[0])
    second_number=float(seprated_math_string[2])
    operator=seprated_math_string[1]


    return calculate_mathematical_expression(first_number, second_number
                                             , operator)

