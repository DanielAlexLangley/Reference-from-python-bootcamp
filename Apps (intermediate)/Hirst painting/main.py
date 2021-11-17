
# https://pypi.org/project/colorgram.py/
# https://docs.python.org/3/library/turtle.html

from turtle import Screen
import turtle as t
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# 10 by 10 rows of spots.
# Each dot should be around 20 in size.
# Each dot spaced apart by 50 paces.

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
