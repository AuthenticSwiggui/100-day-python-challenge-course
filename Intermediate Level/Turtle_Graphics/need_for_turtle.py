from turtle import Turtle, Screen
import random

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}


#Initializes turtle screen and places the bid asking which turtle will be the winner
def screen_initialization() -> str:
    screen.setup(width=500, height=400)
    return screen.textinput(title="Bet!", prompt="Which turtle will win? Enter a color! ").lower()

#Generates a list with turtles regarding the colors placed on colors list
def turtle_booting() -> list[Turtle]:
    for color in colors:
        turtles[color] = Turtle()
        turtles[color].color(color)
    return turtles

#Places the turtles ond the starting line
def turtle_init(turtles: list[Turtle]) -> None:
    count = 0
    MARGIN = 20
    for tim in turtles.values():
        #Checks if the turtle's quantity is different to 1 and calculates the spacing between turtles
        if not len(turtles) == 1:
            effective_range =  400 - (MARGIN * 2)
            screen_spaces = effective_range/(len(turtles) -1) 
            y_pos = (count * screen_spaces)-200 + MARGIN
        else:
            y_pos = 0
        print(y_pos)
        tim.penup()
        tim.goto(x=-240, y=y_pos)
        tim.shape("turtle")
        count += 1

#Moves the turtle by a random ammount of steps
def turtle_move(turtle: Turtle) -> None:
    steps = random.randint(1, 10)
    print(steps)
    turtle.forward(steps)

#Runs the race and determines which is the winner
def race(turtles: list[Turtle]) -> str:
    while True:
        for color, turtle in turtles.items():
            turtle_move(turtle)
            current_pos = round (turtle.xcor(), 0)
            if current_pos > 230:
                return color

#Displays the race results
def race_results(bid: str, winner: str) -> None:
    if bid == winner:
        print("You Won!")
    else:
        print("You lose!")
    print(f"The winner was {winner}")

def main() -> None:
    bid = screen_initialization()
    turtles = turtle_booting()
    turtle_init(turtles)
    winner = race(turtles=turtles)
    race_results(bid=bid, winner=winner)   

    screen.exitonclick()
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()

