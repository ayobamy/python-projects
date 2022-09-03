# Hangman
import random
import stringA  lphabet = set(string.ascii_uppercase)
    used_letters = set()

    while (len(word_letters) > 0):
        # used letters
        print("You have uses these letters: ", " ".join(used_letters))

        # current word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ")
        user_letter = user_letter.upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remover(user_letter)

        elif user_letter in used_letters:
            print("You\'ve already used that letter. Please try again.")

        else:
            print("Invalid character. Try again.")



hangman()
