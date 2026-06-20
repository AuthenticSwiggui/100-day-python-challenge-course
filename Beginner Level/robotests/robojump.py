def move_right():
    for i in range(0,3,1):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    move_right()
    move()
    move_right()
    move()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
