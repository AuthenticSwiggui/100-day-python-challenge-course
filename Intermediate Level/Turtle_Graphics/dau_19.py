from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

ANGLE_ROTATION = 10
LENGTH_MOVE = 10

def move_forwards() -> None:
    tim.forward(LENGTH_MOVE)

def move_backwards() -> None:
    tim.backward(LENGTH_MOVE)

def rotate_left() -> None:
    tim.left(ANGLE_ROTATION)
    

def rotate_right() -> None:
    tim.right(ANGLE_ROTATION)

def reset() -> None:
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()