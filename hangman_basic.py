import random

word_list = ["apple", "banana", "caramel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for char in range(word_length):
    display += '_'
print(display)

end_of_game = False

while True:
    if not end_of_game:
        guess = input('Guess a letter: ').lower()
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(display)
        if '_' not in display:
            end_of_game = True
            print('You win')
            break