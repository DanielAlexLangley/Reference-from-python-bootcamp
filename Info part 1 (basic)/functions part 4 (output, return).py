# FUNCTIONS WITH OUTPUTS
# "Return" is the output keyword
# that means when I call this function later on by typing my_function() in my code,
# the output will replace the 'my_function()'
# can then save the output to another variable


def my_function():
    result = 2 * 2
    return result


output = my_function()
print(output)


# Title Case is where first letter is capitalized in each word
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("DanIEL", "LAngleY")
print(formatted_string)


# Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    f"Result: {formatted_f_name} {formatted_l_name}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Already used functions with outputs.
length = len(formatted_name)


# Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


# What if user typed in empty first or last name?
# Use early return
# Prints "None" since no output, so could add print("You didn't provide valid inputs") in the early return section
def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"Result: {formatted_f_name} {formatted_l_name}")
    print("TEST TEST TEST")


# return ENDS THE FUNCTION. If you put instructions after the return, the instructions will be ignored
# see the print instruction after the return instruction above

print(format_name(input("What is your first name? "), input("What is your last name? ")))
# CAN put input commands inside the function inputs
