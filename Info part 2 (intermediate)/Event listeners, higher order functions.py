
from turtle import Turtle, Screen

# Event listeners:
# Need a way to listen to things the user does,
# like when user presses a key on the keyboard.

# In turtle graphics is some screen events.
# The listen method allows the turtle screen to start listening
# and waiting for events the user might trigger, like tapping on a key.

tim = Turtle()
screen = Screen()

# To listen for events, we have to tell screen object to start listening,
# then bind a function that will be trigger when particular key is pressed.
# To bind a keystroke to an event in our code, we have to use an event listener.
# https://docs.python.org/3/library/turtle.html#turtle.listen
# turtle.onkey(fun, key)
# It expects a function with no arguments, and a key like the "a" key on your keyboard.

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
# If we use a function as an argument/input, we don't add parentheses at the end.
screen.exitonclick()

# Higher order functions
# Idea is that it's a function that can work with other functions.
# So onkey() is a higher order function since it can take another
# function as an input then working with it inside its body.
# It's very useful when we need to listen for events then trigger a particular function.
# This is commonly used in Python.

# When using methods you haven't created yourself (like onkey) to use
# keyword arguments rather than position, especially if the position has no meaning.

