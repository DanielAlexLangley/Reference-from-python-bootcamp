
# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/labs/lab01/colors
# https://trinket.io/docs/colors


from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
tim.shape("arrow")
tim.color("black")


# Challenge 1:
# draw a square that is 100 by 100
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# Challenge 2:
# Draw a dashed line, meaning draw line for 10 paces, then no line for 10 paces, then repeat it 15 times total
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Challenge 3:
# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon.
# Each shape should have random color.
# Each side is length 100.
# To get the correct angle, divide 360 by number of sides of the shape.
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# Challenge 4:
# Draw a random walk.
# Random movements north, each, south, or west, after progressing the same distance each time.
# Make a thicker line too.
# Speed up so it draws faster.
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.hideturtle()
# tim.pensize(8)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(directions))
#     tim.forward(20)


# Challenge 5:
# Create a truly random color.
t.colormode(255)  # documentation says this changes the colormode
# We can now create a random color.
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# tim.hideturtle()
# tim.pensize(8)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(20)


# Challenge 6:
# Create spirograph: a number of circles, each with radius of 100, change tilt a little each time.
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
tim.hideturtle()
tim.pensize(1)
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100, extent=None, steps=None)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)


screen = Screen()
screen.exitonclick()
