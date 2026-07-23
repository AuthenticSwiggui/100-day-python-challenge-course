from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.init_scoreboard()

    def init_scoreboard(self) -> None:
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.print_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(arg=f"Your Score: {self.score}", move=False, align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        self.goto(0, -20)
        self.write(arg=f"Your Score: {self.score}", move=False, align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)