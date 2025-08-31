"""
Rock-Paper-Scissors (Player vs Player)
- Player 1 and Player 2 choose rock, paper, or scissors.
- Game compares choices and declares a winner.
"""


print("......rock.......")
print("......paper......")
print(".....scissors....")

print("\n")
player1 = input("Player 1, make your choice, please: ")
print(".....NO CHEATING.....\n"*25)
player2 = input("Player 2, make your choice, please: ")
print("\n")

# Compare choices
if player1 == player2:
	print("Tie, let's try again!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player 1 wins!")
	elif player2 == "paper":
		print("Player 2 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("Player 1 wins!")
	elif player2 == "scissors":
		print("Player 2 wins!")
elif player1 == "scissors":
	if player2 == "paper":
		print("Player 1 wins!")
	elif player2 == "rock":
		print("Player 2 wins!")
else:
	print("Something went wrong!")