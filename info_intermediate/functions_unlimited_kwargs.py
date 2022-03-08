
# KWARG's
# AKA UNLIMITED KEYWORD ARGUMENTS
# THIS USES A DOUBLE ASTERISK

print("Example 1:")
def calculate(**kwargs):  # The kwargs that get passed through are a dictionary.
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    print(kwargs["multiply"])
print(calculate(add=3, multiply=5))

print("Example 2:")
# All these things above you can do lets you look through all the inputs, find the ones you want, then do something.
# Like this is a calculator function...
def calculate2(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate2(2, add=3, multiply=5)

print("Example 3:")
# Can use this when initializing an object.
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

# print("Example 4:")
# # But what if you only pass in make and not model?
# class Car1:
#     def __init__(self, **kwargs):
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
# my_car1 = Car1(make="Nissan")
# print(my_car1.make)
# # It will crash/error. Why?
# # It's expecting model but not finding one. Solution?
# # Use .get

print("Example 5:")
class Car2:
    def __init__(self, **kw):  # Can name this something other than kwargs, like kw.
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car2 = Car2(make="Nissan")
print(my_car2.make)
print(my_car2.model)  # Returns none since we didn't pass anything in for this kwarg.
