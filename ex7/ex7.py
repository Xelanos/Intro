EMPTY_STRING = ''


def print_to_n(n):
    if n < 1:
        return
    if n == 1:
        print(1)
    else:
        print_to_n(n-1)
        print(n)


def print_reversed(n):
    if n < 1:
        return
    if n == 1:
        return print(n)
    else:
        print(n)
        print_reversed(n-1)


def has_divisor_smaller_then(n, i):
    """
    :param n: an int
    :param i: an int
    :return: True if n has a divisor smaller then i(included) False if not.
    (other then the obvious 1)
    """
    if i == 2:
        if (n % i) != 0:
            return False
        else:
            return True
    else:
        return (n % i) == 0 or has_divisor_smaller_then(n, i-1)


def is_prime(n):
    if n < 1:
        return False
    square_root = int(n**0.5)  # first divisor possible is sqrt(n) rounded
    if has_divisor_smaller_then(n, square_root):
        return False
    else:
        return True


def divisors_rec(n, i, list_divisors=None):
    """
    :param list_divisors: a list of current divisors (starts as empty list)
    :param n: an int
    :param i: an natural number (int and >0)
    :return: returns a list of the natural divisors of n starting from i,
    going down.
    """
    if list_divisors is None:
        list_divisors = []
    if i == 1:
        return list_divisors.insert(0,i)
    else:
        if n % i == 0:
            list_divisors.insert(0,i)
            divisors_rec(n, i-1, list_divisors)
            return list_divisors
        else:
            divisors_rec(n, i-1, list_divisors)
            return list_divisors


def divisors(n):
    """

    :param n: an int
    :return: a list of all the natural divisors of n going down.
    0 has no divisors
    """
    if n == 0:
        return []
    divisor = abs(n)
    divisor_list = divisors_rec(n, divisor,)
    return divisor_list


def factorial(n):
    """
    :param n: an int
    :return: n! (1*2*3*...*n)
    """
    if n == 1:
        return n
    else:
        return factorial(n-1) * n


def exp_n_x(n, x):
    if n == 0:
        return 1
    else:
        return exp_n_x(n-1, x) + (x**n)/factorial(n)


def play_hanoi(hanoi, n, src, dest, temp):
    pass


def print_binary_sequences_with_prefix(prefix, n, binary_list=None):
    if binary_list is None:
        binary_list = []
    if n < 1:
        print(EMPTY_STRING)
    else:
        if n == 1:
            binary_list.append(prefix)
        else:
            pass




print_binary_sequences_with_prefix(0,2)

def print_binary_sequences(n):
    if n < 1:
        pass


def print_sequences(char_list, n):
    pass


def print_no_repetition_sequences(char_list, n):
    pass


def no_repetition_sequences_list(char_list, n):
    pass

