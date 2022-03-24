
# Instructions:
# `time.time()` will return the current time in seconds since January 1, 1970, 00:00:00
# Try running the starting code to see the current time printed.
# If you run the code after a while, you'll see a new time printed.
# e.g. first run:
# 1598524371.736911
# second run:
# 1598524436.357875
# The time difference = second run - first run
# 64.62096405029297
# (approx 1 minute)
# Given the above information, complete the code exercise by
# printing out the speed it takes to run the `fast_function()` vs the `slow_function()`.
# You will need to complete the `speed_calc_decorator()` function.
# Expected Output:
# fast_function run speed: 1.1887366771697998s
# slow_function run speed: 15.808910131454468s
# => None
# HINT: You can use `function.__name__` to get the name of the function,
# SOLUTION: https://repl.it/@appbrewery/day-54-1-solution

import time


def speed_calc_decorator(function):
    def wrapper_function():
        seconds_before = time.time()
        function()
        seconds_after = time.time()
        print(f"{function.__name__} run speed: {seconds_after - seconds_before}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


def main():
    fast_function()
    slow_function()


if __name__ == "__main__":
    main()
