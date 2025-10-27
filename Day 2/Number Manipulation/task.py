bmi = 84 / 1.65 ** 2
print(bmi)

#Changing data type can oversimplify and remove decimal places that are imp
print(int(bmi))

#Round function allows you to round decimal numbers correctly
print(round(bmi))

#You can round to a certain limit using n(digits)
print(round(bmi, 2))

#Assignment Operator
score = 0
#If user scores a point
score += 1

print(score)

#if user loses a point
score -= 1
print(score)

#if user doubles points
score *= 2
print(score)

score /= 2
print(score)

#f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")