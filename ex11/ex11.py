#!/usr/bin/env python3

import math

EPSILON = 1e-5
DELTA = 1e-3
SEGMENTS = 100


def plot_func(graph, f, x0, x1, num_of_segments=SEGMENTS, c='black'):
    """
    plot f between x0 to x1 using num_of_segments straight lines
    to the graph object. the function will be plotted in color c
    """
    delta = (x1 - x0) / num_of_segments
    start_point = (x0, f(x0))
    for i in range(num_of_segments):
        end_point = (start_point[0] + delta, f(start_point[0] + delta))
        graph.plot_line(start_point, end_point, c)
        start_point = end_point


def const_function(c):
    """return the mathematical function f such that f(x) = c
    >>> const_function(2)(2)
    2
    >>> const_function(4)(2)
    4
    """
    return lambda x: c


def identity():
    """return the mathematical function f such that f(x) = x

    >>> identity()(3)
    3
    """
    return lambda x: x


def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    >>> sin_function()(math.pi/2)
    1.0
    """
    return lambda x: math.sin(x)


def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    return lambda x: g(x) + h(x)


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    return lambda x: g(x) - h(x)


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    return lambda x: g(x) * h(x)


def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    return lambda x: g(x) / h(x)


def reverse_function(f):
    """:return: (-f)"""
    minus_f = sub_functions(const_function(0), f)
    return minus_f


def solve(f, x0=-10000, x1=10000, epsilon=EPSILON):
    """
    Find a solution to f in the range x0 and x1
    assuming that f is monotnic.
    If no solution was found return None
    """

    def binary_solve(g, starting_x, ending_x):
        """
        binary search to find solution in log time.
        checks for a solution between starting_x to ending_x
        :return: an x such a |f(x)|< epsilon (in float)
        """
        while starting_x <= ending_x:
            mid_point = (starting_x + ending_x) / 2
            if math.isnan(mid_point):
                return mid_point
            if g(mid_point) <= -epsilon:
                # if we are lower then -epsilon we need to search right side
                starting_x = mid_point
            elif g(mid_point) >= epsilon:
                # if we are higher then epsilon we need to search left side
                ending_x = mid_point
            else:
                # if both are false we are in range, and therefore it's the
                # solution
                return mid_point
        return ending_x if (f(ending_x) < f(starting_x)) else starting_x

    if not f(x0) * f(x1) < 0:
        return None
    # If we have a monotonic up function we can use it for binary_solve.
    # if it is monotonic down, we take (-f) which is monotonic up with the same
    # solution
    if f(x1) > f(x0):
        return binary_solve(f, x0, x1)
    else:
        minus_f = reverse_function(f)
        return binary_solve(minus_f, x0, x1)


def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x"""
    def g_inverse(y):
        if y == 0:
            lower_bound = -1
            upper_bound = 1
        else:
            upper_bound = max(y / 2, -y / 2)
            lower_bound = min(y / 2, -y / 2)

        def function_to_solve(x): return g(x) - y
        sol = solve(function_to_solve, lower_bound, upper_bound, epsilon)
        while sol is None:
            lower_bound += lower_bound / 2
            upper_bound += upper_bound / 2
            sol = solve(function_to_solve, lower_bound, upper_bound, epsilon)
        return sol

    return g_inverse


def compose(g, h):
    """return the f which is the compose of g and h """
    return lambda x: g(h(x))


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    return lambda x: ((g(x+delta) - g(x)) / delta)


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    >>> definite_integral(const_function(3),-2,3)
    15.0
    """
    delta = (x1 - x0) / num_of_segments
    current_x = x0 + delta  # starting from x+delta because going back for sum
    integral_sum = 0

    for i in range(num_of_segments):
        riemann_sum = f(current_x - delta / 2) * delta
        integral_sum += riemann_sum
        current_x += delta

    return integral_sum


def integral_function(f, delta=0.01):
    """return F such that F'(x) = f(x)"""
    def F(x):
        num_of_segments = math.ceil(abs(x) / delta)
        if x > 0:
            return definite_integral(f, 0, x, num_of_segments)
        if x < 0:
            return definite_integral(reverse_function(f), x, 0,num_of_segments)
        else:
            return 0
    return F


def ex11_func_list():
    """return list with the functions in q.13"""
    func_list = []
    two = const_function(2)
    x = identity()
    x_square = mul_functions(x, x)
    cos = derivative(sin_function())
    # function 0
    func_list.append(const_function(4))

    # function 1
    func_list.append(sub_functions(const_function(3), sin_function()))

    # function 2
    func_list.append(compose(sin_function(),
                             sub_functions(x, const_function(-2))))

    # function 3
    two_sin_x_square = sum_functions(two,
                                     sum_functions(sin_function(), x_square))
    func_list.append(div_functions(const_function(10), two_sin_x_square))

    # function 4
    func_list.append(div_functions(cos, sub_functions(sin_function(), two)))

    # function 5
    point_three_x_square = mul_functions(const_function(0.3), x_square)
    point_seven_x = mul_functions(const_function(0.7), x)
    quadric = sum_functions(point_three_x_square,
                            sub_functions(point_seven_x, const_function(-1)))
    func_list.append(mul_functions(const_function(-1),
                                   integral_function(quadric)))

    # function 6
    cos_sin = compose(cos, sin_function())
    point_three_cos = mul_functions(const_function(0.3), cos)
    func_list.append(mul_functions(sub_functions(cos_sin,point_three_cos),two))

    # function 7
    x_qubed = mul_functions(x_square, identity())
    func_to_inverse = sub_functions(const_function(2), x_qubed)
    func_list.append(inverse(func_to_inverse))

    return func_list


# func that genrate the figure in the ex description
def example_func(x):
    return (x/5)**3


if __name__ == "__main__":
    import tkinter as tk
    from ex11helper import Graph
    # un-tag the following lines to activate the doctests
    # import doctest
    # doctest.testmod()
    master = tk.Tk()
    graph = Graph(master, -10, -10, 10, 10)
    # un-tag the line below after implementation of plot_func
    # plot_func(graph,example_func,-10,10,SEGMENTS,'red')
    color_arr = ['black', 'blue', 'red', 'green', 'brown', 'purple',
                 'dodger blue', 'orange']
    # un-tag the lines below after implementation of ex11_func_list
    # for f in ex11_func_list():
    #     plot_func(graph, f, -10, 10, SEGMENTS, 'red')

    master.mainloop()
