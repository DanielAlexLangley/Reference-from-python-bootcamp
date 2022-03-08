
# ARGUMENTS WITH DEFAULT VALUES
# This lets you set default values for keyword arguments.
# This lets you give custom value(s) when you call the function.
def my_function(a=1, b=2, c=3):
    return a + b + c
print(my_function(), my_function(a=2))

# You can mix default values with no default values:
def my_function2(a, b=2, c=3):
    return a + b + c
print(my_function2(8))
print(my_function2(a=9))
print(my_function2(8, 4))
