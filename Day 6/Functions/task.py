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


#Code for Hurdles 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_left()
        jump()
    else:
        move()

#Code for Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def wall_trace():
    if right_is_clear():
        turn_right()


while not at_goal():
    wall_trace()
    if wall_in_front():
        turn_left()
    else:
        move()