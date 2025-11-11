def get_username():
    name = input("What's your name?")
    print("Hello " + name)

get_username()

def get_details():
    residence = input("Enter your full street address")
    print("You live in " + residence)


get_details()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


hurdles = range(0, 6)
while not at_goal() == True:
    jump()
