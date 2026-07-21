from turtle import Screen
import time
from snake import Snake

BG_PATH = "Intermediate Level/Snake-Game/source/bgkusuriya.png"

snake = Snake()
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
    while game_running:
        screen.update()
        time.sleep(0.1)
        snake.move()

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
