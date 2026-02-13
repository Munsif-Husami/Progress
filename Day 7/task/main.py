import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

guess = input("Guess a letter: ").lower()

display = ""

display = ""
for harf in chosen_word:
    if harf == guess:
        display += guess
    else:
        display += "_"


# TODO-2: Change the for loop so that you keep the previous correct letters in display.

matches = []

guess2 = input("Guess again :")

while display != chosen_word:
    for harf in chosen_word:
        if harf == guess2:
            matches += guess2
            display += guess2


print(display)

#Here's what your flowchart should map out:
# START
# ↓
# Initialize (word selection, lives, matches list, etc.)
# ↓
# WHILE LOOP starts (game not over)
# ↓
# Set display to empty string
# ↓
# Get player's guess (input)
# ↓
# FOR LOOP through each letter in chosen_word
#
# Is letter == current guess? → Add to matches
# Is letter == current guess OR in matches? → Add letter to display
# Otherwise → Add underscore to display
# ↓
# Print display
# ↓
# Check win/loss conditions
# All letters found? → WIN, exit loop
# Out of lives? → LOSE, exit loop
# Otherwise → loop continues
# ↓
# END
#
# Key things to show in your flowchart:
#
# The nested structure: while loop contains the input, which contains the for loop
# Where variables reset (display = "" each turn)
# Where variables accumulate (matches grows)
# Decision points (diamonds): equality checks, win/loss checks
#
# Would you like me to clarify any specific part of this flow before you draw it out?