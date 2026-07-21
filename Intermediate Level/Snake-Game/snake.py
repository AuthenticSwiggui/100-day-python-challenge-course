from turtle import Turtle

SNAKE_SIZE = 20
MOVE_DISTANCE = 20
ANGLE_ROTATION = 90

UP = 90 
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.snake_tails = []
        for _ in range(3):
            self.add_tail() 
        self.snake_head = self.snake_tails[0]
        

    def display_snake(self) -> None:
        count = 0
        for snake in self.snake_tails:
            x_pos = count * -SNAKE_SIZE
            print(x_pos)
            snake.goto(x_pos, 0)
            count += 1

    def add_tail(self) -> None:
        snake = Turtle()
        snake.penup()
        snake.color("teal")
        snake.shape("circle")
        self.snake_tails.append(snake)

    def move_up(self) -> None:
        if not self.snake_head.heading() == DOWN:
            self.snake_head.setheading(UP)

    def move_down(self) -> None:
        if not self.snake_head.heading() == UP:
            self.snake_head.setheading(DOWN)

    def move_left(self) -> None:
        if not self.snake_head.heading() == RIGHT:
            self.snake_head.setheading(LEFT)
        

    def move_right(self) -> None:
        if not self.snake_head.heading() == LEFT:
            self.snake_head.setheading(RIGHT)
        

    def move(self) -> None:
        for tail_num in range(len(self.snake_tails) -1, 0, -1):
            new_pos = self.snake_tails[tail_num-1].pos()
            self.snake_tails[tail_num].goto(new_pos)
            
        self.snake_head.forward(MOVE_DISTANCE)
        