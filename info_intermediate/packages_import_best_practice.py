
# Format of code below is:
# import module_name
import turtle

# To create a new turtle after this would be:
tim = turtle.Turtle()

# Because of the confusion that can come from using the other ways of importing,
# it can actually be better/preferable to use just the basic "import turtle" version,
# so that anyone reading the code will know the source of the method, since to write
# methods you would have to write the module it came from:
# tim = turtle.Turtle() which shows the source of the method.

# The main reason to use from turtle import Turtle version is when you will be making...
# ...a ton of objects and don't want to have to write out long name = turtle.Turtle() one hundred times.
# But only do this if you can make it be not confusing to later readers.
