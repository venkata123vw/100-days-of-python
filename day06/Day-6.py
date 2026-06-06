# Day 6 - Functions & Reeborg's World

# Custom turn_right function (Reeborg only has turn_left)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Jump over hurdle function
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Maze solver
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Hurdle 1 - repeat function
def repeat_fun():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    repeat_fun()

# Hurdle 4 - jump over hurdles
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()