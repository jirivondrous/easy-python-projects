"""
Number Guessing Game
- Computer picks a random number (1–MAX_NUMBER).
- Player guesses until correct.
- Tracks attempts and allows replay.
"""

import random

# set highest number to choose from
MAX_NUMBER = 10

def random_pick():
    number = random.randint(1, MAX_NUMBER)
    return number

print()
print('----- Welcome to Number Guessing -----\n')

number_to_guess = random_pick()
attempts = 0

while True:
    user_input = input(f'Guess a number 1-{MAX_NUMBER}: ')

    try:
        guess = int(user_input)
            
        attempts += 1
        if guess == number_to_guess:
            print()
            print('You got it right!')
            if attempts > 1:
                print(f'You needed {attempts} guesses.\n')
            else:
                print(f'You needed {attempts} guess.\n')
            
            play_again = input('Do you want to play again? (y/n): ').lower()
            if play_again == 'y':
                attempts = 0
                number_to_guess = random_pick()
            else:
                print('Thank you for playing!')
                break
        elif guess < number_to_guess:
            print('TOO LOW!')
        else:
            print('TOO HIGH!')
    except ValueError:
        print('Please enter a valid number!')
        continue