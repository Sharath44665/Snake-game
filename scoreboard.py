from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score} ", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", move=False, align=ALIGNMENT, font=FONT)
    def collide_over(self):
        self.clear()
        self.write(f"Snake collapsed, Score: {self.score}, GAME Over ", move=False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.clear()
        self.write(f"Score: {self.score}, GAME Over ", move=False, align=ALIGNMENT, font=FONT)