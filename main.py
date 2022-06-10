from turtle import Screen
from  snake import Snake
from food import Food
import time

my_screen=Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title(titlestring="Snake Game")
my_screen.tracer(0) #tracer off


snake=Snake()
food =Food()

my_screen.listen()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")
game_status=True
while game_status:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) <15:
        food.refresh()


my_screen.exitonclick()

