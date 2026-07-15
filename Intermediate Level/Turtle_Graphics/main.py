from turtle import Turtle, Screen

jhonny_the_turtle = Turtle()



def lefty():
    jhonny_the_turtle.forward(100)
    jhonny_the_turtle.right(90)

jhonny_the_turtle.shape("turtle")
jhonny_the_turtle.color("cyan")
screen = Screen()

for _ in range(4):
    lefty()


def dashed_line(steps: int, turtle: Turtle) -> None:
    turtle.pendown()
    turtle.forward(steps)
    turtle.penup()
    turtle.forward(steps)


for _ in range(50):
    dashed_line(steps=10, turtle=jhonny_the_turtle)


screen.exitonclick()