
# ARG's
# AKA UNLIMITED POSITIONAL ARGUMENTS (positional since the position you pass in an argument matters)
# THE NAME ARG STANDS FOR ARGUMENT
# THIS USES A SINGLE ASTERISK

def add1(n1, n2):
    return n1 + n2
print(add1(n1=5, n2=6))

# What if you wanted to add more than 2 numbers?
# How to allow any number of arguments to be used as inputs?
def add2(*args):
    total = 0
    for n in args:  # These arguments can be looped through, and they are in the form of a tuple.
        total += n
    return total
print(add2(1, 2, 3, 4))

# You can also access things by index, since it's a tuple:
def add3(*args):
    print(args)  # This is with no index.
    print(args[0])  # This is with an index.
print(add3(50))
