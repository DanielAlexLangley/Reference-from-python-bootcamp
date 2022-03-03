
# LIST COMPREHENSION
# WORKS WITH SEQUENCES, LIKE LISTS, STRINGS, RANGE, TUPLE
# A list comprehension is where you create a new list from a previous list.

# Previously, we've done it using a for loop:
# (Example: add 1 to each item in the list):
print("Intro exercises:")
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# In list comprehension, we can take those 4 lines of code and turn them into 1:
# new_list = [new_item for item in list]
# "new_list" is the name of the new list
# "new_item" is the n + 1 code
# "n" is the variable name we give to each item we're going to loop through.
# "list" is the list we're going to iterate through.
new_list = [n + 1 for n in numbers]
print(new_list)

# Example with string:
name = "Angela"
new_list = [letter for letter in name]
# This takes each letter and puts them into a list.
print(new_list)

# Create range 1,5, loop through it, create list where each number is doubled. Final list should be 2,4,6,8:
doubled_numbers = [number * 2 for number in range(1, 5)]
print(doubled_numbers)

# CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]
# "test" is the condition you're checking for.
# Code only happens if check is passed.
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Make new list with names that have less than 5 letters:
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Create list of longer names, and make them all uppercase:
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
print("\n")

print("Exercise 1:")
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Write a List Comprehension to create a new list called "squared_numbers".
# New list should contain every number in the list "numbers" but each number should be squared.
# Do not change the code above. Write your 1 line code below:
squared_numbers = [number**2 for number in numbers]
# Write your code above.
# Example output: [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
print(squared_numbers)
print("\n")

print("Exercise 2:")
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# New list called "result" should only contain the even numbers from the list "numbers".
# Do not change the code above. Write your 1 line code below:
result = [number for number in numbers if (number % 2) == 0]
# Write your code above.
# Example output: [2, 8, 34]
print(result)
print("\n")

print("Exercise 3:")
# Create list called result which contains the numbers that are common...
# ...in both comprehension_lists_file1.txt and comprehension_lists_file2.txt.
# Result should be a list that contains Integers, not Strings. Do not use a loop.
# Example output: [3, 6, 5, 33, 12, 7, 42, 13]
# Write your code below:
with open("comprehension_lists_file1.txt") as file:
    contents_file1 = [int(item.strip("\n")) for item in file.readlines()]
with open("comprehension_lists_file2.txt") as file:
    contents_file2 = [int(item.strip("\n")) for item in file.readlines()]
result = [number for number in contents_file1 if number in contents_file2]
# My version that I made is above.
print(result)

# The teacher's version is below:
with open("comprehension_lists_file1.txt") as file1:
    list1 = file1.readlines()
with open("comprehension_lists_file2.txt") as file2:
    list2 = file2.readlines()
result = [int(num) for num in list1 if num in list2]
print(result)
print("\n")
