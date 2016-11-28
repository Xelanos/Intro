import math


def create_list():
    """A function that takes multiple inputs from the user
    and returns each input in a block of a list.
    function ends when user inputs ''(does not add '')
    """
    i = 0
    user_strings_list = list()
    while i >= 0:
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
    """A function that takes a list of numbers
    and returns their sum
     """
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


print(average([]))

def cyclic(lst1,lst2):
    pass

def histogram(n,num_list):
    pass

def prime_factors(n):
    pass

def cartesian(lst1, lst2):
    pass

def pairs(n,num_list):
    pass
