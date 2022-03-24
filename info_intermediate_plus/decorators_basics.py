
# Decorator:
# A decorator is a function.
# A decorator is a function that expects ANOTHER function as parameter
# A decorator function is a function that gives additional functionality to an existing function.
# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484

# ********Day 54 Start**********
# Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


# Python functions are known as first class objects.
# That means you can pass a function around as an argument, just like you can do with an integer, string, or float.
# That means we can take the above functions and use them to build other functions.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)
result = calculate(add, 2, 3)
print(result)


# Functions can be nested in other functions
def outer_function():
    print("I'm outer")
    def nested_function():
        print("I'm inner")
    nested_function()
outer_function()


# Functions can be returned from other functions
def outer_function2():
    print("I'm outer")
    def nested_function():
        print("I'm inner")
    return nested_function
inner_function = outer_function2()
inner_function()


# Simple Python Decorator Functions
# A decorator function is a function that wraps another function and gives it some additional functionality.
import time
def delay_decorator(function):  # This is the decorator function in this example.
    def wrapper_function():
        time.sleep(2)
        # If you wanted to add some functionality before the function, you would add it here.
        function()
        # If you wanted to add some functionality after the function, you would add it here.
    return wrapper_function

@delay_decorator  # This decorator will apply to the function in the line immediately below it ("say_hello"):
def say_hello():
    print("Hello")
say_hello()

# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()
# This example is another way to do it, but this is not the preferred way.
# The preferred way is to use the @ syntactic sugar way.

# With the @ syntactic sugar
# "Syntactic sugar" is syntax you can write to make it easier to write an alternative line of code.
@delay_decorator  # This syntax @ then the name is called "syntactic sugar".
def say_bye():
    print("Bye")
say_bye()
