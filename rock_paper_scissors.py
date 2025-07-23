print("......rock.......")
print("......paper......")
print(".....scissors....")

print("\n")
print("Player 1, make your choice, please: ")
player1=input()

print(".....NO CHEATING.....\n"*25)

print("Player 2, make your choice, please: ")
player2=input()
print("\n")

# choices are made now compare them (rock, paper, scissors)

if player1 == player2:
	print("Tie, try again.")
elif player1 == "rock" and player2 == "paper":
	print("Player 2 wins.")
elif player1 == "rock" and player2 == "scissors":
	print("Player 1 wins.")
elif player1 == "paper" and player2 == "rock":
	print("Player 1 wins.")
elif player1 == "paper" and player2 == "scissors":
	print("Player 2 wins.")
elif player1 == "scissors" and player2 == "paper":
	print("Player 1 wins.")
elif player1 == "scissors" and player2 == "rock":
	print("Player 2 wins.")
else:
	print("something went wrong!")