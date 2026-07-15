import turtle as turtly
import random

from turtle_color_list import turtle_colors
from turtle import Screen



turtly.shape("turtle")
turtly.color("green")
s = Screen()

def draw_figures(sides: int):
    turtly.color(random.choice(turtle_colors))
    for _ in range(sides):
        angle = 360/sides
        turtly.right(angle)
        turtly.forward(50)

for i in range(3, 1000):
    draw_figures(i)

s.exitonclick()