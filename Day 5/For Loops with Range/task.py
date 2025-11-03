#Range function with for loops

#for number in range (1,25, 2):
#    print(number)

sum_el = 0
#
# for number in range(1,101):
#     sum_el += number
# print(sum_el)

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)