EMPTY_STRING = ''
SPACE = ' '


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
        return list_divisors.insert(0, i)
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
    """
    make a list of all binary sequences of length n starting with 'prefix'
    :param prefix: the prefix required : 1 or 0
    :param n: length of desired  list
    :param binary_list: variable for memorizing for the recursion
    :return: a list of lists, each inner list represent a sequence starting
    """
    if binary_list is None:
        binary_list = []
    if n < 1:
        return print(EMPTY_STRING)
    else:
        if n == 1:
            binary_list.append([str(prefix)])
            return binary_list
        else:
            # getting all the lists of n-1 length
            binary_list = print_binary_sequences_with_prefix(prefix,n-1
                                                             ,binary_list)
            # for every sequence in the n-1 list, add one with '1' in the
            # end and one with '0'
            final_list = []
            for seq in binary_list:
                final_list.append(seq + ['1'])
                final_list.append(seq + ['0'])

            binary_list = final_list[:]
            return binary_list


def concat_list(chr_list):
    """
    Takes a list of lists of strings, an returns a string of the inner
    lists joined, seperated by space
    exemple : [[1,2][2,1]] will get 12 21
    """
    final_print = ''
    for list in chr_list:
        final_print += ''.join(list) + SPACE
    return final_print


def print_binary_sequences(n):
    zero_sequences_list = print_binary_sequences_with_prefix(0, n)
    one_sequences_list = print_binary_sequences_with_prefix(1, n)
    final_list = zero_sequences_list + one_sequences_list
    for seq in final_list:
        print(''.join(seq))


def print_char_sequences_with_prefix(prefix, char_list, n, cr_list=None):
    """
    make a list of all possible sequences consisting of char list
      of length n starting with 'prefix'
    :param prefix: the prefix required : any one letter
    :param char_list: a list of chars
    :param n: length of desired  list
    :param cr_list: variable for memorizing for the recursion
    :return: a list of lists, each inner list represent a sequence starting
    """
    if cr_list is None:
        cr_list = []
    if n < 1:
        return print(EMPTY_STRING)
    else:
        if n == 1:
            cr_list.append([prefix])
            return cr_list
        else:
            # getting all the lists of n-1 length
            cr_list = print_char_sequences_with_prefix(prefix,char_list, n-1,
                                                             cr_list)
            # for every sequence in the n-1 list, add a sequence with
            # a diffrent char from the char list
            final_list = []
            for seq in cr_list:
                for char in char_list:
                    final_list.append(seq + [char])

            cr_list = final_list[:]
            return cr_list


def print_sequences(char_list, n):
    """Print all possible sequences of lenth n consisting form
     chars from the char list
    """
    printing_list = []
    for character in char_list:
        printing_list.extend(print_char_sequences_with_prefix
                             (character, char_list,n))
    for seq in printing_list:
        print(''.join(seq))



def print_no_repetition_sequences(char_list, n):
    pass


def no_repetition_sequences_list(char_list, n):
    pass

