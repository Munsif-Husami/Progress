print("My age: " + str(12)) #Concatenation
print(123+456) #Addition
print(456435-243423) #Subtraction
print(3*2) #Multiplication
print(6/3) #Division
#Divisions always give us a float type answer - this is default in Python because
#Python implicitly converts this into floating points.

#the following division operator changes this to plain int types
print(6//3) #Clean Division

#If its not a clear division then don't use this because it removes all decimals, example -
print(5//3)

print(5**5) #Exponent, 5 raised to 5 basically (5^5) in Plain English
print(2**64)

#Remember the PEMDAS rule - when multiple operators order is \n
# Parentheses, exponents, multiplication, division, addition and subtraction. Example -

print(3 * (3 + 3)/3 - 3)