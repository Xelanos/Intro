import hangman_helper
PATTERN_SPACE = '_'


def letters_in_pattern(pattern):
    """A function that takes a pattern and returns a list of the letters
    in it, without doubles.
    """
    list_of_letters = []
    for i in range(len(pattern)):
        if pattern[i] == PATTERN_SPACE:
            continue
        elif pattern[i] in list_of_letters:
            continue
        else:
            list_of_letters.append(pattern[i])
    return list_of_letters


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
    reveled at the all appropriate locations.
    """
    word_listed = list(word)
    pattern_listed = list(pattern)
    for (i, letter_in_word) in enumerate(word_listed):
        if letter_in_word == letter:
            pattern_listed[i] = letter
        # turn list back to string
    updated_pattern = concat_list(pattern_listed)

    return updated_pattern


def check_word_against_pattern(pattern, word):
    """A function that takes a pattern and a word of the same length
    and returns true if the word fits the pattern (same letters in
    the same places) and false if not
    """
    pattern_letters = letters_in_pattern(pattern)
    for i in range(len(pattern)):
        if pattern[i] == PATTERN_SPACE:
            if word[i] in pattern_letters:
                return False
            else:
                continue
        elif pattern[i] != word[i]:
            return False
    return True


def filter_words_list(words_list, pattern, wrong_guess_lst):
    """A function that takes a list of words(strings) and current pattern
    (also string) as well as a list of letters guessed wrong and filters
    the list of words to word that match the pattern and without the
    wrong letters in them.
    returns a list of the filtered words.
    """
    words_filtered = words_list[:]  # shadow copy to work with
    for word in words_list:
        list_of_word = list(word)

        # remove word if word is not the same length as pattern
        if len(word) != len(pattern):
            words_filtered.remove(word)
            continue

            # remove word if does not fit the reveled pattern
        if not check_word_against_pattern(pattern, word):
                words_filtered.remove(word)
                continue

            # remove if contains a letter already known as wrong
        for letter in wrong_guess_lst:
            if letter in list_of_word:
                if word in words_filtered:
                    words_filtered.remove(word)
    return words_filtered


CHAR_A = 97


def letter_to_index(letter):
    """
    Return the index of the given letter in an alphabet list.
    """
    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """
    Return the letter corresponding to the given index.
    """
    return chr(index + CHAR_A)


def list_to_max_letter(abc_indexes):
    """A function that take a list of 25 ints corresponding the the ABC
    and returns one letter corresponding to the largest index on the list
    """
    max_value = max(abc_indexes)
    max_index = abc_indexes.index(max_value)
    max_letter = index_to_letter(max_index)
    return max_letter


def choose_letter(words, pattern):
    """A function that takes a list of words and a pattern and returns
    the letter that appears most in the words of the list that aren't already
    in the pattern.
    :return: the letter that appears the most
    """
    pattern_letters = letters_in_pattern(pattern)
    list_of_indexes = []   # after finding the largest index
                           # we will covert back to letter
    for index in range(25):
        counter = 0  # start counting at 0 for each index
        letter = index_to_letter(index)

        # if already in pattern, add 0
        if letter in pattern_letters:
            list_of_indexes.append(counter)
            continue
        # count letters in each word
        else:
            for word in words:
                for k in range(len(word)):
                    if letter == word[k]:
                        counter += 1
        list_of_indexes.append(counter)
    max_letter = list_to_max_letter(list_of_indexes)
    return max_letter


def checking_valid_input(expected_letter):
    """A function that takes a string an return true if it is a valid input
    valid input is 1 lowercase letter.
    """
    if expected_letter.islower():
        if len(expected_letter) == 1:
            return True
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

        # if user wants a hint
        if user_choice == hangman_helper.HINT:
            filtered_words = filter_words_list(words_list, pattern,
                                               wrong_guesses_list)
            hint = choose_letter(filtered_words, pattern)
            printed_massage = hangman_helper.HINT_MSG + hint
            continue

        # if user inputs a letter
        if user_choice == hangman_helper.LETTER:
            # checking if valid
            if checking_valid_input(user_input):
                if user_input not in chosen_letters:
                    # if input is correct, update pattern or add mistake
                    if user_input in list_of_the_word:
                        pattern = update_word_pattern(random_word, pattern,
                                                      user_input)
                        chosen_letters.append(user_input)
                        printed_massage = hangman_helper.DEFAULT_MSG
                    else:
                        errors += 1
                        wrong_guesses_list.append(user_input)
                        chosen_letters.append(user_input)
                        printed_massage = hangman_helper.DEFAULT_MSG
                else:
                    printed_massage = hangman_helper.ALREADY_CHOSEN_MSG \
                                      + user_input
                    continue
            else:
                printed_massage = hangman_helper.NON_VALID_MSG
                continue

        # if guessed the whole word, end the game.
        if pattern == random_word:
            hangman_helper.display_state(pattern, errors, wrong_guesses_list,
                                         hangman_helper.WIN_MSG, True)
            return None

    # if got out of the loop, user must have lost.
    hangman_helper.display_state(pattern, errors, wrong_guesses_list,
                                 hangman_helper.LOSS_MSG + random_word, True)
    return None


def main():
    """Runs the game, repeat if user wants to"""
    the_word_list = hangman_helper.load_words()
    run_another_game = True
    while run_another_game:
        run_single_game(the_word_list)
        run_another_game = hangman_helper.get_input()[1]


if __name__ == "__main__":
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()
