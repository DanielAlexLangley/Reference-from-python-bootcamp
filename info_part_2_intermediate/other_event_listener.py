
from turtle import Turtle, Screen

# Event listeners:
# Need a way to listen to things the user does,
# like when user presses a key on the keyboard.

# In turtle graphics is some screen events.
# The listen method allows the turtle screen to start listening
# and waiting for events the user might trigger, like tapping on a key.


# To listen for events, we have to tell screen object to start listening,
# then bind a function that will trigger when particular key is pressed.
# To bind a keystroke to an event in our code, we have to use an event listener.
# https://docs.python.org/3/library/turtle.html#turtle.listen
# turtle.onkey(function, key)
# It expects a function with no arguments, and a key like the "a" key on your keyboard.


def move_forwards():
    tim.forward(10)


tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forwards)
# If we use a function as an argument/input, we don't add parentheses at the end.
screen.exitonclick()
