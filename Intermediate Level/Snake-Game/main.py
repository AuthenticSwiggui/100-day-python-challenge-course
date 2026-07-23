from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BG_PATH = "Intermediate Level/Snake-Game/source/bgkusuriya.png"

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()

game_running = True

def screen_setup() -> None:
    screen.setup(width=600, height=600)
    screen.bgpic(BG_PATH)
    screen.title("Authentic Snaky")
    screen.tracer(0)

def key_mapping() -> None:
    screen.listen()
    screen.onkey(key="w", fun=snake.move_up)
    screen.onkey(key="s", fun=snake.move_down)
    screen.onkey(key="a", fun=snake.move_left)
    screen.onkey(key="d", fun=snake.move_right)
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)
    
def move_snake() -> None:
    game_running = True
    while game_running:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.snake_head.distance(food) <= 15:
            food.place_food()
            snake.add_tail()
            scoreboard.add_point()
        x = snake.snake_head.xcor()
        y = snake.snake_head.ycor()

        if not (-300 <= x <= 280) or not (-280 <= y <= 280):
            game_running = False
            scoreboard.game_over()

        for tail in snake.snake_tails[1:]:
            if snake.snake_head.distance(tail) < 10:
                    game_running = False
                    scoreboard.game_over()


def main() -> None:
    screen_setup()      
    key_mapping() 
    snake.display_snake()
    move_snake()

    
    screen.exitonclick()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
