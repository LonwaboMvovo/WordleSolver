import re
import requests
import random
import string


def get_words() -> list:
    # S/O https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3
    # Get list of 5 letter english words from meaningpedia.com
    meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
    # compile regex
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    # return all matches
    return pattern.findall(meaningpedia_resp.text)


def survey_says(the_word, current_guess, num_tries, all_guesses):
    playing_game = True

    all_guesses.append(current_guess)

    if current_guess == the_word:
        print("noice")
        playing_game = False
    elif not num_tries:
        print("not noice")
        playing_game = False

    # checking letters
    
    
    return playing_game, num_tries - 1, all_guesses
    

if __name__ == "__main__":
    word_list = get_words()
    valid_letters = string.ascii_lowercase
    invalid_letters = ""
    all_guesses = []

    # L+
    the_word = "ratio"

    num_tries = 5

    # First guess
    #  A pair of MIT researchers said its the best starting word idk
    current_guess = "salet"
    print(f"Lets try {current_guess}")
    playing_game, num_tries, all_guesses = survey_says(the_word, current_guess, num_tries, all_guesses)

    while playing_game:
        print("Unluck")

        current_guess = random.choice(word_list)
        print(f"Lets try {current_guess}")

        playing_game, num_tries, all_guesses = survey_says(the_word, current_guess, num_tries, all_guesses)


    print(all_guesses)