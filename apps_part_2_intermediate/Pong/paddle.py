
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # The default size of the square is 20 x 20 pixels.
        # By doing stretch_wid=5, that multiples 20 by 5 which equals 100. This gets us our rectangle paddle we want.
        # stretch_len=1 means the length will not change.
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
