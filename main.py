import requests
import random


def get_words():
    # S/O https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3
    # S/0 https://github.com/tabatkins/wordle-list

    # Get list of 5 letter english words from meaningpedia.com
    wordle_word_list_resp = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/main/words")
    return wordle_word_list_resp.text.split("\n")


def check_letters(placed_letters, current_guess):
    new_invalid_letters = ""

    franken_word = ["", "", "", "", ""]

    letter_colours = input("Colours: ").lower()

    for franken_index in range(5):
        letter = current_guess[franken_index]
        letter_colour = letter_colours[franken_index]

        if letter_colour == "g":
            placed_letters += letter

        if letter_colour == "b" and letter not in placed_letters:
            new_invalid_letters += letter

        franken_word[franken_index] = letter_colour + letter

    return new_invalid_letters, franken_word, placed_letters


def remove_invalid_words(word_list, invalid_letters, franken_word):
    # remove words containing invalid letters
    for word in word_list.copy():
        removed_words = []

        for letter in invalid_letters:
            if word not in removed_words and letter in word:
                word_list.remove(word)
                removed_words.append(word)

    # remove words that don't have green letters
    for word in word_list.copy():
        removed_words = []

        for letter_index in range(len(franken_word)):
            letter_colour = franken_word[letter_index][0]
            letter = franken_word[letter_index][1]

            if ((word not in removed_words) and
                    (letter_colour == "g" and word[letter_index] != letter)):
                word_list.remove(word)
                removed_words.append(word)

    # remove words that don't have yellow letters
    for word in word_list.copy():
        removed_words = []

        for letter_index in range(len(franken_word)):
            letter_colour = franken_word[letter_index][0]
            letter = franken_word[letter_index][1]

            if ((word not in removed_words) and
                    (letter_colour == "y" and letter not in word)):
                word_list.remove(word)
                removed_words.append(word)

    # remove words that don't have green letters
    for word in word_list.copy():
        removed_words = []

        for letter_index in range(len(franken_word)):
            letter_colour = franken_word[letter_index][0]
            letter = franken_word[letter_index][1]

            if ((word not in removed_words) and
                    (letter_colour == "y" and word[letter_index] == letter)):
                word_list.remove(word)
                removed_words.append(word)
    return word_list


def survey_says(franken_word, current_guess, num_tries, all_guesses, word_list):
    playing_game = True

    all_guesses.append(current_guess)

    if all("g" == colour_letter[0] for colour_letter in franken_word):
        print("\n*****\nnoice\n*****\n")
        print(f"It took {6-num_tries} guesses and there were {len(word_list)} {'words' if len(word_list) > 1 else 'word'} left to choose from:")
        playing_game = False
    elif not num_tries or not len(word_list):
        print("\n*********\nnot noice\n*********\n")
        print(f"There were {len(word_list)} {'words' if len(word_list) > 1 else 'word'} left to choose from:")
        playing_game = False    
    return playing_game, num_tries - 1, all_guesses
    

if __name__ == "__main__":
    word_list = get_words()
    placed_letters = ""
    invalid_letters = ""
    all_guesses = []

    num_tries = 5

    # First guess
    # A pair of MIT researchers said its the best starting word idk
    current_guess = "salet"
    print("According to a pair of MIT researchers\"SALET\" is statistically the best word to start with")
    print(f"So, lets try {current_guess}")

    invalid_letters, franken_word, placed_letters = check_letters(placed_letters, current_guess)
    word_list = remove_invalid_words(word_list, invalid_letters, franken_word)
    playing_game, num_tries, all_guesses = survey_says(franken_word, current_guess, num_tries, all_guesses, word_list)

    # TODO to clean up this do while loop can make word_list only have "salet" at first then when num_tries is 5 can use the full word list
    while playing_game:
        print("Unluck")

        current_guess = random.choice(word_list)
        print(f"\nLets try {current_guess}")

        while input("Is the word valid? ").lower() == "n":
            word_list.remove(current_guess)
            current_guess = random.choice(word_list)
            print(f"\nOK then lets try {current_guess}")

        invalid_letters, franken_word, placed_letters = check_letters(placed_letters, current_guess)
        word_list = remove_invalid_words(word_list, invalid_letters, franken_word)
        playing_game, num_tries, all_guesses = survey_says(franken_word, current_guess, num_tries, all_guesses, word_list)

    print(word_list)

    print("\nThese were all the guesses:\n",all_guesses)