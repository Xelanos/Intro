import math


def quadratic_equation(a, b, c):
    """A function that returns the solution/s of
    an quadratic equation by using it's coefficients
     """
    discriminant = math.pow(b, 2) - 4 * a * c  # Discriminant variable
    if a == 0:
        first_solution = (-c) / b
        second_solution = None

    # no solutions
    elif discriminant < 0:
        first_solution = None
        second_solution = None

    # one solution
    elif discriminant == 0:
        first_solution = ((-b) + math.sqrt(discriminant)) / 2 * a
        second_solution = None

    # two solutions
    elif discriminant > 0:
        first_solution = ((-b) + math.sqrt(discriminant)) / 2 * a
        second_solution = ((-b) - math.sqrt(discriminant)) / 2 * a

    return first_solution, second_solution


def numbers_extract(user_string):
    """A function that takes a string in the from of
    'NUMBER-space-NUMBER-space-NUMBER'
    and returns those numbers in float """
    spilt_string = user_string.split()

    # extracting the numbers
    spilt_a = float(spilt_string[0])
    spilt_b = float(spilt_string[1])
    spilt_c = float(spilt_string[2])
    return spilt_a, spilt_b, spilt_c


def quadratic_equation_user_input():
    """A function that lets user input coefficients for
     a quadratic equation and prints the solution/s
     of said equation
     """
    math_string = input("Insert coefficients a, b, and c: ")
    user_a, user_b, user_c = numbers_extract(math_string)

    # getting the results
    solution_1, solution_2 = quadratic_equation(user_a, user_b, user_c)

    # print the results #
    # no solutions
    if solution_1 is None and solution_2 is None:
        print('The equation has no solutions')

    # one solution
    elif solution_1 is not None and solution_2 is None:
        print('The equation has 1 solution: ' + str(solution_1))

    # two solutions
    else:
        print('The equation has 2 solutions: '
              + str(solution_1) + ' and ' + str(solution_2))
