def get_username():
    name = input("What's your name?")
    print("Hello " + name)

get_username()

def get_details():
    residence = input("Enter your full street address")
    print("You live in " + residence)


get_details()

#Code for Hurdles 2

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


#Code for Hurdles 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
