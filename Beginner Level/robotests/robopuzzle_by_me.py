def decide():
    
    while not front_is_clear():
        move_right()
        if wall_in_front():
            turn_left()
            turn_left()
    
    move()
        
        
def move_right():
    for i in range(0,3,1):
        turn_left()


while not at_goal():
    decide()