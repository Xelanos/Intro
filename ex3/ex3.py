import math


def create_list():
    """A function that takes multiple inputs from the user
    and returns each input in a block of a list.
    function ends when user inputs ''(empty string)(does not add '')
    """
    i = 0
    user_strings_list = list()
    while i >= 0:  # runs until hitting break condition
        string_from_user = input()
        if string_from_user == '':
            break
        else:
            user_strings_list.append(string_from_user)
    return user_strings_list


def concat_list(str_list):
    """A function that takes a list of strings and return one
    string compromised from them all
     """
    complete_user_string = ''
    for i in range(len(str_list)):
        complete_user_string = complete_user_string + str_list[i]

    return complete_user_string


def list_sum(list_of_numbers):
    """A function that takes a list of numbers and returns their sum"""
    total_sum = float()
    for i in range(len(list_of_numbers)):
        total_sum += float(list_of_numbers[i])
    return total_sum


def average(num_list):
    """A function that takes a list of numbers
        and returns their average
         """
    if len(num_list) == 0:
        return None
    else:
        total_list_sum = list_sum(num_list)
        # average is total sum divided by number of numbers
        list_average = total_list_sum / len(num_list)
        return list_average


def the_list_cycler(user_list_input, m):
    """A joyful ride for lists that takes a list and cycle it
    by 'm' spaces.
    for cyclic lists see ex3 pdf
     """
    cycled_list = user_list_input[:]  # shadow copy to copy length
    for i in range(len(user_list_input)):
        # each index in the original goes to the ((i+m)%list size) index
        new_index = (i+m) % (len(user_list_input))
        cycled_list[new_index] = user_list_input[i]
    return cycled_list


def cyclic(lst1, lst2):
    """A function that check if lst2 and lst1 are cyclic lists of each other.
    returns true if they are, false if they are not.
    for for cyclic lists see ex3 pdf.
    """
    if lst1 == [] and lst2 == []:
        return True
    elif len(lst1) != len(lst2):
        return False
    else:
        for i in range(len(lst1)):
            # cycle each time by i, i increase until list length
            lst2_cycled = the_list_cycler(lst2, i)
            if lst1 == lst2_cycled:
                return True
    return False


def list_num_checker(number, list_of_numbers):
    """A function that takes a number and a list of integers
    and return how many times the number appears in the list
    """
    number_counter = 0
    for i in range(len(list_of_numbers)):
        if number == int(list_of_numbers[i]):
            number_counter += 1
    return number_counter


def histogram(n, num_list):
    """A function that prints out the histogram list of the number n
    from the list num_list
    for histogram see: https://en.wikipedia.org/wiki/Histogram """
    i = 0
    histogram_list = []
    while i < n:
        # checks how many times i is in the list, and adds to histogram_list
        # 'i'th location. (using append since i=0 at start)
        how_many_times = list_num_checker(i, num_list)
        histogram_list.append(how_many_times)
        i += 1
    return histogram_list


def is_prime(num):
    """returns true if the number is prime, false if not"""
    for divisor in range(2, int(math.sqrt(num))+1):
        if num % divisor == 0:
            return False
    return True


def all_prime_up_to(m):
    """returns all prime numbers up to m in a list"""
    primes = list()
    for i in range(2, m):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_factors(n):
    """A function that takes a number and returns a list of it's prime factors
    for prime factors: https://en.wikipedia.org/wiki/Prime_factor
    """
    prime_list = all_prime_up_to(n)
    if n < 2:  # not interested in 2,1 or 0
        return []
    prime_factors_list = list()
    for p in prime_list:
        if p*p > n:  # prime cannot be more the square of number
            break
        while n % p == 0:
            # check how many times p is dividing the current n, then adds p
            # to list of factors the number of times it's dividing n and makes
            # a new n without the prime factors we already found
            prime_factors_list.append(p)
            n //= p
    if n > 1:
        # if the leftover n is not 1 it MUST also be a prime
        prime_factors_list.append(n)
    return prime_factors_list


def cartesian(lst1, lst2):
    """A function that takes 2 lists and return their cartesian product.
    if one list is empty, returns an empty list.
    return type is a tuple of lists. (if one of the lists is empty returns
    empty list).
    for cartesian product: https://en.wikipedia.org/wiki/Cartesian_product
    """
    list_of_cartesian_paris = list()
    if len(lst1) == 0 or len(lst2) == 0:
        return []
    for i in lst1:
        for k in lst2:
            tuple_to_add = (i, k)
            list_of_cartesian_paris.append(tuple_to_add)
    return list_of_cartesian_paris


def check_sum(num1, num2, c):
    """A function that takes 2 int numbers (num1 and num2)
    and returns true if their sum is c. (if not returns false)
    """
    if (num1 + num2) == c:
        return True
    else:
        return False


def list_cleanup(user_list):
    """A function that takes a list of DIFFERENT pairs of ints, and
    if there are two pairs with the same numbers, deletes one
    of the pairs.
    returns the "clean" list.
    """
    for i in user_list:
        for k in user_list:
            if i == k:  # do not check pair with itself
                continue
            elif cyclic(i, k):   # if pairs are cyclic, removes the later
                user_list.remove(k)
    return user_list


def pairs(n, num_list):
    """A function that takes an int n and a list of ints
    and find pairs of numbers in the list such as that their sum is n.
    returns list of the pairs mentioned above
    """
    pair_list = list()
    for i in range(len(num_list)):
        for k in range(len(num_list)):
            if i == k:  # cannot add the same number
                continue
            elif check_sum(int(num_list[i]), int(num_list[k]), n):
                # if the sums of the numbers is n, make them a pair and adds
                # to the list.
                add_to_list = [num_list[i], num_list[k]]
                pair_list.append(add_to_list)
    clean_pair_list = list_cleanup(pair_list)  # clean the list from duplicates

    return clean_pair_list

