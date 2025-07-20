import random

# set highest number to choose from
MAX_NUMBER = 10

def random_pick():
    number = random.randint(1, MAX_NUMBER)
    return number


print('----- Welcome to Number Guessing -----')

number_to_guess = random_pick()
count = 0

while True:
    user_input = input(f'Guess a number 1-{MAX_NUMBER}: ')

    try:
        guess = int(user_input)
    
        count += 1
        if guess == number_to_guess:
            print('You got it right!')
            if count > 1:
                print(f'You needed {count} guesses.\n')
            else:
                print(f'You needed {count} guess.\n')
            
            play_again = input('Do you want to play again? (y/n): ').lower()
            if play_again == 'y':
                count = 0
                number_to_guess = random_pick()
            else:
                print('Thank you for playing!')
                break
        elif guess < number_to_guess:
            print('TOO LOW!')
        else:
            print('TOO HIGH!')
    except: #ValueError
        print('Please enter a valid number!')
        continue