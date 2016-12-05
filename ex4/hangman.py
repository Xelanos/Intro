from ex4 import hangman_helper


def concat_list(str_list):
    """A function that takes a list of strings and return one
    string compromised from them all
     """
    complete_user_string = ''
    for i in range(len(str_list)):
        complete_user_string = complete_user_string + str_list[i]

    return complete_user_string


def update_word_pattern(word, pattern, letter):
    """A function that takes a single word(string) of all
    lowercase letters , the current reveled pattern(string)
    and a letter, and returns the updated pattern with the letter guessed
    reveled at the appropriate locations.
    """
    word_listed = list(word)
    pattern_listed = list(pattern)
    for (i, letter_in_word) in enumerate(word_listed):
        if letter_in_word == letter:
            pattern_listed[i] = letter
            # turn list back to string
            updated_pattern = concat_list(pattern_listed)

    return updated_pattern


def checking_valid_input(expected_letter):
    """A function that takes a string an return true if it is a valid input
    valid input is 1 lowercase letter.
    """
    if len(expected_letter) != 1:
        return False
    elif expected_letter.islower():
        return True
    else:
        return False


def run_single_game(words_list):
    """chooses one word out of the word list in random and starts
    a game of hangman with said word.
    in the end, wait for input from the user as to weather
    start a new game or not.
    for hangman see: https://en.wikipedia.org/wiki/Hangman_(game)
    """
    # variable list with starting conditions
    random_word = hangman_helper.get_random_word(words_list)
    chosen_letters = []
    wrong_guesses_list = []
    list_of_the_word = list(random_word)
    pattern = '_' * len(random_word)
    printed_massage = hangman_helper.DEFAULT_MSG
    errors = 0

    # the smart part
    while errors < hangman_helper.MAX_ERRORS:
        hangman_helper.display_state(pattern, errors, wrong_guesses_list,
                                     printed_massage,)
        user_choice, user_input = hangman_helper.get_input()

        if user_choice == hangman_helper.HINT:
            printed_massage = hangman_helper.NO_HINTS_MSG

        if user_choice == hangman_helper.LETTER:
            if checking_valid_input(user_input):  # checking if valid
                if user_input not in chosen_letters:
                    # if input is correct, update pattern or add mistake
                    if user_input in list_of_the_word:
                        update_word_pattern(random_word, pattern, user_input)
                        chosen_letters.append(user_input)
                    else:
                        errors += 1
                        wrong_guesses_list.append(user_input)
                        chosen_letters.append(user_input)
                        printed_massage = hangman_helper.DEFAULT_MSG
                else:
                    printed_massage = hangman_helper.ALREADY_CHOSEN_MSG \
                                      + user_input
            else:
                printed_massage = hangman_helper.NON_VALID_MSG

        # if guessed the whole word, end the game.
        #  and ask for input (for new game)
        if pattern == random_word:
            hangman_helper.display_state(pattern, errors, wrong_guesses_list,
                                         hangman_helper.WIN_MSG, True)
            return hangman_helper.get_input()

    # if got out of the loop, user must have lost.
    #  asks for input in case of  new game
    hangman_helper.display_state(pattern, errors, wrong_guesses_list,
                                 hangman_helper.LOSS_MSG + random_word, True)
    return hangman_helper.get_input()








