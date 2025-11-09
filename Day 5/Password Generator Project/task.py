letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
# import random
# pw_list = ""
#
# for char in range(0, nr_letters):
#     pw_list += random.choice(letters)
#
# for sym in range(0, nr_symbols):
#     pw_list += random.choice(symbols)
#
# for num in range(0, nr_numbers):
#     pw_list += random.choice(numbers)
#
# print(pw_list)
# print(f"Your password is {pw_list}")

#You're a stupid fuck because you needed to look at the code. FUCK YOU. NEVER let Claude show you code.
# \n You struggled 3 days with no code for what? Just to forget to tell Claude no code.
# \n Weakling. You got this. Never again.


#Hard Level
import random
pw = []
# for char in range(0, nr_letters):
#     pw += random.choice(letters)
#
# for sym in range(0, nr_symbols):
#     pw += random.choice(symbols)
#
# for num in range(0, nr_numbers):
#     pw += random.choice(numbers)

#Keep in mind += and append() do the same thing here. You're just adding data to the list here.

for char in range(0, nr_letters):
    pw.append(random.choice(letters))

for sym in range(0, nr_symbols):
    pw.append(random.choice(symbols))

for num in range(0, nr_numbers):
    pw.append(random.choice(numbers))

#Version of printing password using join() function
print(pw)
random.shuffle(pw)
password = "".join(pw)
print(f"Your password is {password}")

#Version of printing password using string concatenation

print(pw)
random.shuffle(pw)
password = ""
for each in pw:
    password += each
print(f"Your password is {password}")
