import colorgram
from turtle import Turtle, Screen
import random

IMAGE_PATH = "Intermediate Level/Turtle_Graphics/source/Imagen1.jpg"
COLOR_COUNT = 10


def extract_colors() -> list[float]:
    colors = colorgram.extract(IMAGE_PATH, COLOR_COUNT)


    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors

def move_grid():
    colors = extract_colors()
    turtly.hideturtle()
    y_pos = -150
    for _ in range(10):
        x_pos = -150
        for _ in range(10):
            turtly.teleport(x_pos, y_pos) 
            paint_dot(colors)
            x_pos += 50
        y_pos += 50
        
def paint_dot(color_list: list[float]) -> None:
    r, g, b = random.choice(color_list)
    turtly.dot(20, r, g, b) 


turtly = Turtle()

screen = Screen()
screen.colormode(255)
move_grid()

screen.exitonclick()