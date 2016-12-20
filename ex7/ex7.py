def print_to_n(n):
    if n == 1:
        print(1)
    else:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    if n == 1:
        return print(n)
    else:
        print(n)
        print_reversed(n-1)

def has_divisor_smaller_then(n, i):
    pass

def is_prime(n):
    pass


def divisors(n):
    pass


def factorial(n):
    """
    :param n: an int
    :return: n!
    """
    if n == 1:
        return n
    else:
        return factorial(n-1) * n


def exp_n_x(n, x):
    if n == 1:
        return 1
    else:
        return exp_n_x(n-1, x) + (x**n)/factorial(n)


def play_hanoi(hanoi, n, src, dest, temp):
    pass


def print_binary_sequences(n):
    pass


def print_sequences(char_list, n):
    pass


def print_no_repetition_sequences(char_list, n):
    pass


def no_repetition_sequences_list(char_list, n):
    pass

