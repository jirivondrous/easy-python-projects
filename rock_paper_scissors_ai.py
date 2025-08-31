import random

#Images
rock_img = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_img = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_img = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Welcome message
print("===== Welcome to Rock, Paper, and Scissors Game! =====\n")

#User's choice
user_choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

print()
print("You chose:")

if user_choice == "0":
    user_choice = 'rock'
    print(rock_img)
elif user_choice == "1":
    user_choice = 'paper'
    print(paper_img)
else:
    user_choice = 'scissors'
    print(scissors_img)

#PC random choice
print("Computer chose:")

pc_random = random.randint(0, 2)

if pc_random == 0:
    pc_choice = 'rock'
    print(rock_img)
elif pc_random == 1:
    pc_choice = 'paper'
    print(paper_img)
else:
    pc_choice = 'scissors'
    print(scissors_img)

#Determine the winner
if user_choice == pc_choice:
    print("It's a tie!")
elif user_choice == 'rock':
    if pc_choice == 'scissors':
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 'paper':
    if pc_choice == 'rock':
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 'scissors':
    if pc_choice == 'paper':
        print("You win!")
    else:
        print("You lose!")
