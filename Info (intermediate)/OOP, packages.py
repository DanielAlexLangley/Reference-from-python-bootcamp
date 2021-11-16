
import turtle
from turtle import Screen
from prettytable import PrettyTable


text1 = '''
The old way of programming was called procedural programming.
I have no notes about that old way.
New way of programming is object oriented programming.
AKA OOP

"Objects" are a way of combining data (the attributes) and functionality (the methods) all in same thing.
"What it has, and what it does."
What is has are attributes (which are variables that are associated with/attached to that model object aka blueprint).
What it does are methods (a method is a function that is tied to an object).

We can generate multiple versions of the same object, as many as we want from the same blueprint.
The blueprint/type is called a "class".

The individual objects that are generated from the class are called "objects".
The objects are what we use in our code.

To create a new object from a class looks like:
car = CarBlueprint()
"car" is the object
"CarBlueprint()" is the class

Convention says to capitalise first letter of each word in BluePrint() name instead of separating by underscores...
This is called "Pascal Case".

When making an object, most people name the object the same as the blueprint...
...except all in lowercase and words separated by underscores.
So an object made from "CarBlueprint()" would probably be named car_blueprint 

Turtle Graphics is a library that will let us put graphics onto the screen.
This library comes preloaded in every download of python, so we should already have it installed.
See these links:
https://docs.python.org/3/library/turtle.html
https://cs111.wellesley.edu/labs/lab01/colors

'''


text2 = '''
In this exercise, we're going to create an object from a blueprint (aka class)...
...that someone else has already created.
That blueprint lives in another module called turtle, so we have to import it.
Inside the turtle module is a class called turtle.
The format of the line of code below is:
object_name = module.object()
'''
# import turtle
timmy = turtle.Turtle()  # this line gives us a new turtle object called timmy
print(timmy)


text3 = '''
Alternatively, I could have written:
import turtle
from turtle import Turtle
(after we see we want the "screen" module to, could have written here):
from turtle import Turtle, Screen
timmy = Turtle()
'''


text4 = '''
If we had an object "car" that has attributes "speed" and "fuel"...
To access those attributes:
car.speed
object.attribute

For methods aka functions:
To access a method:
car.stop()
object.method()
'''


text5 = '''
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


text6 = '''
A python package is different from a module since a python package is...
...a whole bunch of code/lots of files other people have written...
...all packaged together for a goal or purpose.

Search for packages on PyPi
https://pypi.org/
This is an index we can pull packages from.

For example:
https://pypi.org/project/prettytable/
Helps us display tables in ascii format.
Click the link to find out more about it:
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

To add a package to a project:
Make sure you have your project open already.
Click "File" in PyCharm
Click "Settings"
Click your project name on the left.
Click "Python Interpreter"
Click the + sign for "install"
Search for the package you want by name.
Click "Install Package"
Click the "X" in the top left window when it's done installing.
'''

# from prettytable import PrettyTable
# in the above line, if you want to see source code of the package...
# you can right click on it > Go To > Implementation(s)
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # change attribute to left aligned
print(table)
