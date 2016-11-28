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
    complete_user_string = ''
    for i in range(len(str_list)):
        complete_user_string = complete_user_string + str_list[i]

    return complete_user_string

print(concat_list(create_list()))
