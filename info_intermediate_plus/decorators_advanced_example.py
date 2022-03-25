
# INSTRUCTIONS:
# Create a logging_decorator() which is going to log the name of the function that was called,
# the arguments it was given and finally the returned output.
# Excepted output:
# You called a_function(1, 2, 3)
# It returned: 6

def logging_decorator(function):
    def wrapper(*args):  # I could have also added **kwargs, but it would have no effect.
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper


@logging_decorator
def a_function(int_one, int_two, int_three):
    return int_one + int_two + int_three


a_function(1, 2, 3)
