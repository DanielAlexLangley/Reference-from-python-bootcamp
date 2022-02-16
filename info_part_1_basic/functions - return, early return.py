
# Return as an early exit
def format_name1(f_name, l_name):
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
    return f"Result: {formatted_f_name} {formatted_l_name}"


# return ENDS THE FUNCTION. If you put instructions after the return, the instructions will be ignored
# see the print instruction after the return instruction above

# CAN put input commands inside the function inputs
print(format_name1(input("What is your first name? "), input("What is your last name? ")))
print(format_name2(input("What is your first name? "), input("What is your last name? ")))

# Storing output in a variable
formatted_name = format_name1(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name1(input("What is your first name? "), input("What is your last name? ")))
# Already used functions with outputs.
length = len(formatted_name)
