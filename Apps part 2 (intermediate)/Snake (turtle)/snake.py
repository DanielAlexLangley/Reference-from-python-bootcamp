
from turtle import Turtle

# She called these "constants" and said constants in Python are
# all caps with snake case for the underscores between words.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # In the range function here, the left number is the number it will start on,
        # the middle number is the number it will stop on,
        # and the right number is the step.
        # (like either 1 or -1 depending on if you want it to step up or step down)
        # So it would look like this if we could include keyword arguments:
        # for seg_num in range(start=2, stop=0, step=-1):
        # in this case, instead of starting on 2, in the future we may add more starting segments,
        # so we will use len(segments) instead of 2.
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
