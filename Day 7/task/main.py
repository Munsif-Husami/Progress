import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""
for harf in chosen_word:
    if harf == guess:
        display += guess
    else:
        display += "_"

print(display)

# TODO-1: - Use a while loop to let the user guess again.

guess_again = input("Guess Again: ").lower()

def repeat_loop():
    print(guess_again)

count = range(word_length)
while not display == chosen_word:
    repeat_loop()

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for index, harf in enumerate(chosen_word):
    if display[0] != "_":


