
# Format of code below is:
# keyword module
import turtle
# To create a new turtle after this would be:
tim = turtle.Turtle()


# If we use that turtle class a lot, then it would be easier to write it like:
# keyword module_name keyword thing_in_module
from turtle import Turtle
# If we write it like that, we can just write:
tim = Turtle()  # rather than have to write tim = turtle.Turtle() so much,
# since we could be making many turtles like tom = Turtle() and terry = Turtle().


# We can import everything from that module by using the asterisk:
from turtle import *
# It can be confusing to import everything, since you may not know where methods come from when you use them later on.
# Because of this confusion, it's unusual in Python community to write code like this.
# Most good programmers won't use this asterisk version.


# Because of this type of confusion, it can actually be better/preferable to use...
# ...just the basic "import turtle" version, so that anyone reading the code will..
# ...know the source of the method, since to write methods you would have to write...
# ...the version that is like: tim = turtle.Turtle() which shows the source of the method.
# The main reason to use from turtle import Turtle version is when you will be making...
# ...a ton of objects and don't want to have to write out long name = turtle.Turtle() one hundred times.
# But only do this if you can make it be not confusing to later readers.


# ALIAS
# The format used below is:
# keyword module_name keyword alias_name
import turtle as t
# Some modules have super long names.
# This brings in the entire module as the alias_name.
# This helps alleviate the issues described above of having to write out long variables hundreds of times.
tim = t.Turtle()


# INSTALLING MODULES
# Turtle is packaged with Python standard library.
# This library is just basic stuff.
# There are many more Python modules and packages out on the internet.
# pypi.org
# If you try to import a module that isn't apart of the library, PyCharm will give you an error message.
# If you click the error message, you can have PyCharm install the module.
# Example:
# import heroes
