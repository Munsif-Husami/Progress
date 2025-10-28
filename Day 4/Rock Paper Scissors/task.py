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
    print("Invalid Response")
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
