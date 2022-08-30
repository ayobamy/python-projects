# Guess the number (user)

import random

def guess_number(num):
  random_num = random.randint(1, num)
  guess_number = 0
  
  while (guess_number != random_num):
    guess_number = input(f"Guess a number between 1 and {num}: ")
    guess_number = int(guess_number)

    if (guess_number < random_num):
      print(f"Sorry! Guess again. {guess_number} is too low")
      
    elif (guess_number > random_num):
      print(f"Sorry! Guess again. {guess_number} is too high")

  print(f"Yayyyy! You've guessed the number {guess_number} right.")

guess_number(100)