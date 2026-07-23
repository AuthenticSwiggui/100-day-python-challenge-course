from turtle import Turtle
import random

class Food(Turtle):

    

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.place_food()

    def place_food(self) -> None:
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
