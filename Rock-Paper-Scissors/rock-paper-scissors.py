# Rock Paper Scissors
import random

# 'r' for rock, 'p' for paper, and 's' for scissors
    # r > s, s > p, p > r

bot_choice = ['r', 'p', 's']

def play():
    player = input("R for rock, P for paper, S for Scissors.\nWhat's your choice?  ")
    player = player.lower()
    computer = random.choice(bot_choice)

    if (player == computer):
        return "It\'s a tie!"

    if is_win(player, computer):
        return "You Won!"

    return "Sorry! You lost!"

def is_win(player, computer):
    if ((player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r')):

        return True

print(play())


