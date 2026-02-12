import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = []

word_size = len(chosen_word)

for abc in chosen_word:
    placeholder.append('_')

print(" ".join(placeholder))

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = []
for harf in chosen_word:
    if harf == guess:
        display.append(guess)
    else:
        display.append("_")

print(" ".join(display))

# TODO-1: - Use a while loop to let the user guess again.

while not display == chosen_word:
    print(input("Guess Again: ").lower())
    for harf in chosen_word:
        if harf == guess:
            display.append(guess)
        else:
            print("You've won! Yay!")

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for harf in chosen_word:
    if harf == guess:
        display += harf
    else:
        display += "_"
        print("You lost a life.")

print(display)
