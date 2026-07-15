import turtle as turtly
import random

from turtle_color_list import turtle_colors
from turtle import Screen

STEPS_TO_MOVE = 30
DIRECTIONS = [0, 90, 180, 270]

def move(steps: int) -> None:
    turtly.color(random.choice(turtle_colors))
    angle = random.choice(DIRECTIONS)

    turtly.setheading(angle)
    turtly.forward(steps)
    
turtly.pensize(10)
turtly.speed(0)

s = Screen()

for _ in range(100):
    move(STEPS_TO_MOVE)

print("Running colors in 255")
###Random colors v2.0
turtly.colormode(255)
def move2(steps: int) -> None:
    r, g, b = random_colors()
    turtly.color(r, g, b)
    
    angle = random.choice(DIRECTIONS)

    turtly.setheading(angle)
    turtly.forward(steps)
    
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(100):
    move2(STEPS_TO_MOVE)

s.exitonclick()