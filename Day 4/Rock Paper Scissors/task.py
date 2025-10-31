rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
    comp_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You won!")
    elif comp_choice == 0 and user_choice == 2:
        print("You lost!")
    elif user_choice > comp_choice:
        print("You won!")
    elif user_choice < comp_choice:
        print("You lost!")
    elif user_choice == comp_choice:
        print("It's a draw!")
elif user_choice < 0 or user_choice >= 3:
    print("Invalid response. You lost!")

