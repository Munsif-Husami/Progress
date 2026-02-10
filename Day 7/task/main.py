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

for alfaaz in chosen_word:
    if alfaaz == guess:
        print("Right")
    else:
        print("Wrong")

display = ""
for harf in chosen_word:
    if harf in guess:
        print(guess)
    else:
        print(" ".join(range(placeholder)))