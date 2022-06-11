from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title(titlestring="Snake Game")
my_screen.tracer(0)  # tracer off

snake = Snake()
food = Food()
my_score = ScoreBoard()

my_screen.listen()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")
game_status = True
while game_status:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        my_score.update_score()
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_status = False
        my_score.game_over()
    # for segment in snake.snake_segment:
    #     if segment==snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 9:
    #         # print(snake.snake_head.distance(segment))
    #         game_status=False
    #         my_score.collide_over()
    #     if snake.snake_head.distance
    # -----------------OR--------------------
    for segment in snake.snake_segment[1:]:
        if snake.snake_head.distance(segment) < 9:
            game_status = False
            my_score.collide_over()

my_screen.exitonclick()
