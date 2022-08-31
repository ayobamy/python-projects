import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
'''

ascii_images = [rock, paper, scissors]
# Ask for user choice
usr_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_choice = random.randint(0, 2)

if usr_choice >= 3 or usr_choice < 0:
	print("You typed an invalid number, you lose!")
else:
	print("You chose {}".format(usr_choice))
	print(ascii_images[usr_choice])
	# Computer choice
	print("Computer chose {}".format(computer_choice))
	print(ascii_images[computer_choice])

	if usr_choice == 0 and computer_choice == 2:
		print("Rock beats Scissors! You win!")
	elif computer_choice == 0 and usr_choice == 2:
		print("Rock beats Scissors! You lose!")
    
	elif (computer_choice > usr_choice):
		if (computer_choice == 1 and usr_choice == 0):
			print("Paper beats Rock! You lose")
		elif (computer_choice == 2 and usr_choice == 1):
			print("Scissors beats Paper! You lose")
      
	elif (usr_choice > computer_choice):
		if (usr_choice == 1 and computer_choice == 0):
			print("Paper beats Rock! You Win!")
		elif (usr_choice == 2 and computer_choice == 1):
			print("Scissors beats Paper! You Win")
      
	elif (computer_choice == usr_choice):
		print("It's a draw")
