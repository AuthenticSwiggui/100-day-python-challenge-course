def decide():
    if front_is_clear():
        move()
    elif right_is_clear():
        move_right()
    else:
        turn_left()
        
        
def move_right():
    for i in range(0,3,1):
        turn_left()


while not at_goal():
    decide()