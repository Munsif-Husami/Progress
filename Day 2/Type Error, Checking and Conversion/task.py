#len('hello')

#How to check different data types using the type command
print(type('Hello'))
print(type(3124523424_3413213_565756))
print(type(.0093102931031))
print(type(True))

#Convert types by using the type name and parentheses
int("123")
print(int("123") + int("456"))

#Type conversions which don't make sense and cause errors - int("abc")
print(type("Number of letters in your name")) #string type
print(type(length)) #int type

user_name = input("Enter your name")
length = len(user_name)

print("Number of letters in your name: " + str(length))

