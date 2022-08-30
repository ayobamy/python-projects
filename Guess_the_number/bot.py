# Guess the number (computer)

import random

def bot_guess(num):
  low = 1
  high = num
  response = ''

  while (response != 'c'):
    if (low != high):
      guess_number = random.randint(low, high)
    else:
      guess_number = low
      
    response = input(f"Is {guess_number} too high (H), too low (L) or correct (C)??  ")
    response = response.lower()
    
    if (response == 'h'):
      high = guess_number - 1
      
    elif (response == 'l'):
      low = guess_number + 1

  print(f"Yayyyy! The bot guessed the number {guess_number} right.")

bot_guess(100)
