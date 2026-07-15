import random
import turtle as t
from turtle import Screen

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

screen = Screen()

MULTIPLIER = 5

t.speed(0)
t.colormode(255)

for i in range(int(360 / MULTIPLIER)):
    t.color(random_colors())
    t.circle(100)
    t.setheading(i * MULTIPLIER)



screen.exitonclick()