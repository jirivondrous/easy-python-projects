"""
Simple Dice Rolling Game
- Asks user if they want to roll
- Rolls two dice and shows results
- Keeps looping until user quits
"""

import random

while True:
    choice = input('Roll the dice? (y = yes, n = no): ').strip().lower()
    
    if choice == "y":
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        print(f'You rolled {die_1}, {die_2}')
    elif choice == "n":
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')
