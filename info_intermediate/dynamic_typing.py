
# Python is unique because it is both strongly, dynamically typed

# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
# "Strong typing means that the type of a value doesn't change in unexpected ways.
# A string containing only digits doesn't magically become a number, as may happen in Perl.
# Every change of type requires an explicit conversion.
# Dynamic typing means that runtime objects (values) have a type,
# as opposed to static typing where variables have a type."

# What is strong typing?
# Strong typing is when a variable has a type.
# If I have a variable called number that is a string, then I type number**2 to find the square root, it won't work.
# number = "x"
# number ** 2
# Python makes you comply with the variable type it's expecting. This is strong typing.

# Dynamic typing:
# Even though Python knows what type a variable is, and it knows what type a function expects...
# ...you can also dynamically change a datatype of any variable like this:
a = 3
print(type(a))
a = "Hello"
print(type(a))
# The fact that I can change the type of variable like this means Python is capable of dynamic typing.
