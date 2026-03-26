import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

word_size = len(chosen_word)

placeholder = ""
for position in range(word_size):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""
matches = []
for harf in chosen_word:
    if harf == guess:
        display += guess
        matches += guess
    else:
        display += "_"

print(display)

# TODO-1: - Use a while loop to let the user guess again.

# while not display == chosen_word:
#     guess_again = input("Guess again").lower()
#     print(guess_again)
#     display = ""
#     for harf in chosen_word:
#         if harf == guess_again:
#             display += harf
#             matches += harf
#         elif harf in matches:
#             display += harf
#         else:
#             display += "_"
#     print(display)
# print("You Win")



# TODO-2: Change the for loop so that you keep the previous correct letters in display.

while not display == chosen_word:
    guess_again = input("Guess again").lower()
    print(guess_again)
    display = ""
    for harf in chosen_word:
        if harf == guess_again:
            display += harf
            matches += harf
        elif harf in matches:
            display += harf
        else:
            display += "_"
    print(display)
print("You Win")

