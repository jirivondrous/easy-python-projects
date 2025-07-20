import random

while True:
    choice = input('Do you want to roll the dice? (y/n): ').lower()
    if choice == "y":
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        print(f'You rolled {die_1}, {die_2}')
    elif choice == "n":
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')
