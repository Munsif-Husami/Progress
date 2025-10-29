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
#Approach 1


#This is not working because any wrong inputs do not stop the game or result in an invalid error message.
#hence I plugged away for 2 days and then tried Approach 2 based on the solution in coursework.
#My code here got too complicated because I tried accounting for each probability as an if statement
#Also I didn't have a way to simplify how to connect the images to the input options for both computer and me.

import random
print("Welcome to Rock, Paper, Scissors!")
yourmove = input("What do you choose?\nType 0 for rock, 1 for paper, 2 for scissors.\n")
comp_choices = ["0","1","2"]
if yourmove == "0":
    print(rock)
elif yourmove == "1":
    print(paper)
elif yourmove == "2":
    print(scissors)
else:
    print("Invalid response")
pc_move = random.choice(comp_choices)
if pc_move == "0":
    print(rock)
elif pc_move == "1":
    print(paper)
elif pc_move == "2":
    print(scissors)
if yourmove == pc_move:
    print("Its a draw")
elif yourmove == "0" and pc_move == comp_choices[1]:
    print("You lose")
elif yourmove == "0" and pc_move == comp_choices[2]:
    print("You win")
elif yourmove == "1" and pc_move == comp_choices[0]:
    print("You win")
elif yourmove == "1" and pc_move == comp_choices[2]:
    print("You lose")
elif yourmove == "2" and pc_move == comp_choices[0]:
    print("You lose")
elif yourmove == "2" and pc_move == comp_choices[1]:
    print("You win")
else:
    print("Invalid response")

# #Approach 2

print("Welcome to rock, paper, scissors!")
yourmove = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
comp_choices = random.randint(0,2)
game_images = [rock,paper,scissors]
if yourmove >= 0 and yourmove <= 2:
    print(game_images[yourmove])
print(f"Computer chose:")
print(game_images[comp_choices])
if yourmove >= 3 or yourmove < 0:
    print("You typed an invalid response.")
elif yourmove == 0 and comp_choices == 2:
    print("You win!")
elif comp_choices == 2 and yourmove == 0:
    print("You lose!")
elif comp_choices > yourmove:
    print("You lose!")
elif yourmove > comp_choices:
    print("You win!")
elif comp_choices == yourmove:
    print("Its a draw!")
