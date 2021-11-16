

# print
# input function
# string concatenation is done with the "+" sign
# \n new line within a string
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)


# len function
name = input("What is your name?")
length = len(name)
print(length)


# variables
a = input("a: ")
b = input("b: ")
c = ""
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)


# data type - string
empty = ""  # will print as a blank line
above = "Blank line above"
print("Blank line below.")
print(empty)
print(above)


# escaping characters
print("Can\'t you see the slash?")


# make string all lower case
choice1 = input('Type a word with some CAPITAL LETTERS in it, then press enter: ').lower()
print(choice1)


# multi-line/multi-block string
# add three single quotes ''' at the start and at the end of a string to turn it into a multi-line string.
multi_line_string = '''Line 1
Line 2
Line 3'''
print(multi_line_string)


# subscript AKA subscripting
print("Hello"[0])
print("Hello"[4])


# subscripting example
# program that adds the digits in a 2 digit number.
# best method
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
# alternative method:
two_digit_number2 = input("Type a two digit number: ")
str_first_number = two_digit_number2[0]
str_second_number = two_digit_number2[1]
print(int(str_first_number) + int(str_second_number))


# f-string
score = 0  # int
height = 1.8  # float
isWinning = True  # boolean
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")


# another way to do f-string is into a variable, like:
whatever1 = 50
whatever2 = 100
example_variable = f"The first number is {whatever1}, and the second number is {whatever2}."
print(example_variable)


# example
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(((total / split) * ((tip / 100) + 1)), 2)}")


# count within a string
# see love calculator for an example

