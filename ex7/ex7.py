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
    """
    :param n: an int
    :param i: an int
    :return: True if n has a divisor smaller then i(included) False if not
    """
    if i == 2:
        if (n % i) != 0:
            return False
        else:
            return True
    else:
        return (n % i) == 0 or has_divisor_smaller_then(n, i-1)


def is_prime(n):
    square_root = int(n**0.5)  # first divisor possible is sqrt(n) rounded
    if has_divisor_smaller_then(n, square_root):
        return False
    else:
        return True


def divisors(n):
    list_of_divisors = []
    if n == 1:
        return list_of_divisors.append(1)
    else:
        pass






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

def print_binary_sequences_with_prefix(prefix,n):
    if n == 1:
        print(prefix)
    else:
        print(print_binary_sequences_with_prefix(prefix,n-1)+str(0),
              print_binary_sequences_with_prefix(prefix,n-1)+str(1))




def print_binary_sequences(n):
    pass


def print_sequences(char_list, n):
    pass


def print_no_repetition_sequences(char_list, n):
    pass


def no_repetition_sequences_list(char_list, n):
    pass

