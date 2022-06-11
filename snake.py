from turtle import Turtle

SNAKE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake_segment = []
        # self.colors_list = ["blue", "green", "red"]
        self.create_snake()
        self.snake_head = self.snake_segment[0]

    def create_snake(self):
        x_val = 0

        for index in range(3):
            self.add_segment(x_val=x_val)
            x_val -= 20

    def add_segment(self, x_val):

        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape(name="square")
        new_turtle.goto(x=x_val, y=0)
        new_turtle.color("white")
        self.snake_segment.append(new_turtle)

    def extend_snake(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape(name="square")
        new_turtle.goto(x=new_turtle.xcor(), y=0)
        new_turtle.color("white")
        self.snake_segment.append(new_turtle)

    def move(self):
        for index_of_snake in range(len(self.snake_segment) - 1, 0, -1):  # 1
            new_x = self.snake_segment[index_of_snake - 1].xcor()
            new_y = self.snake_segment[index_of_snake - 1].ycor()
            self.snake_segment[index_of_snake].goto(x=new_x, y=new_y)
        self.snake_head.forward(SNAKE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
        # pass

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
