import main
import string


word_list = main.get_words()
placed_letters = ""
invalid_letters = ""

correct_word = "ratio"

my_word = "salet"

franken_word = ["", "", "", "", ""]

print("---------")
print(my_word, franken_word)
# check correct letters
for letter_index in range(len(my_word)):
    letter = my_word[letter_index]
    correct_letter = correct_word[letter_index]
    print(letter, correct_letter)
        
    if letter == correct_letter:
        franken_word[letter_index] = "g" + letter
        placed_letters += letter

print("---------")
print(my_word, franken_word)
# check letters in word
for letter_index in range(len(my_word)):
    letter = my_word[letter_index]
    print(letter, correct_word)

    if letter in correct_word and letter not in placed_letters:
        franken_word[letter_index] = "y" + letter
        placed_letters += letter

print("---------")
print(my_word, franken_word)
# deal with remaining letters
for letter_index in range(len(my_word)):
    letter = my_word[letter_index]
    print(letter, correct_word)

    if letter not in placed_letters:
        invalid_letters += letter
        franken_word[letter_index] = "b" + letter

print(my_word, franken_word)
