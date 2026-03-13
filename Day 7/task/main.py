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
    display_reset = ""
    print(guess_again)

matches = []

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

count = range(word_length)
while not display == chosen_word:
    repeat_loop()
    for harf in chosen_word:
        if guess_again in matches or guess_again in chosen_word:
            matches += guess_again
            display += guess_again
            print(display)
        else:
            print(display)

# 3. The for loop syntax:
# You need to decide: do you want to loop through letters or through indices?
#
# for letter in chosen_word: - gives you each letter directly ('c', 'a', 'm', 'e', 'l')
# for i in range(word_length): - gives you positions (0, 1, 2, 3, 4), then you access chosen_word[i]
#
# Both work! Which feels more natural to you?
# If you use letters directly, you check if letter == guess_again or letter in matches
# If you use indices, you check if chosen_word[i] == guess_again or chosen_word[i] in matches
# 4. The condition:
# Right now you have if guess_again in matches - but this asks "is the guess in matches?"
# You should ask: "is the letter I'm currently looking at in matches or equal to the current guess?"
# What variable represents the letter you're currently examining in the loop?
# 5. Where to get the guess:
# Should guess_again = input(...) be inside or outside the while loop? Think: do you want one guess total, or a new guess each turn?
# 6. Updating matches:
# When should you add a letter to matches? After you've checked and confirmed the guess is in the word, right? Where in your code would that check happen?
# Which of these four do you want to tackle first?