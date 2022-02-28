
import turtle
from turtle import Screen


text1 = '''

Turtle Graphics is a library that will let us put graphics onto the screen.
This library comes preloaded in every download of python, so we should already have it installed.
See these links:
https://docs.python.org/3/library/turtle.html
https://cs111.wellesley.edu/labs/lab01/colors

In this exercise, we're going to create an object from a class that someone else has already created.
That blueprint lives in another module called turtle, so we have to import it.
Inside the turtle module is a class called turtle.
'''

# The format of the line of code below is:
# object_name = module.object()
timmy = turtle.Turtle()  # this line gives us a new turtle object called timmy
print(timmy)
# when printing this, it just shows as an object in memory. We need a screen to see it on the screen.
# see below for more info on the screen

text3 = '''
Alternatively, I could have written:
from turtle import Turtle
(after we see we want the "screen" module too, could have written here):
from turtle import Turtle, Screen
timmy = Turtle()

If we had an object "car" that has attributes "speed" and "fuel"...
To access those attributes:
car.speed
object.attribute

For methods aka functions:
To access a method:
car.stop()
object.method()

Another class inside Turtle module is "screen".
Screen is the window in which the turtle will show up.
'''

# from turtle import Screen
my_screen = Screen()
timmy.shape("turtle")  # these methods are listed on the website linked above
timmy.color("red", "green")  # these methods are listed on the website linked above
timmy.forward(100)
print(my_screen.canvheight)
# it prints 300
my_screen.exitonclick()  # if I don't write this line, then the screen shows up then quickly disappears
