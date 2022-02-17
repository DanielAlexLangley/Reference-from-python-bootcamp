
# Dictionaries:
# Every dictionary has two parts to it...
# On left is the key, and the right is the value:
# {Key: Value}

# put a comma after every item, even the last time, so it's ready for a new one to be added
# don't forget to put quotes around keys, or else it will think they are something other than strings
# unless you don't want string, in which case enter it without quotes

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# to retrieve item from dictionary:
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# to add new items to dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# create empty dictionary:
empty_dictionary = {}

# edit item
programming_dictionary["Bug"] = "Bug's new definition."
print(programming_dictionary["Bug"])

# loop through dictionary
for key in programming_dictionary:
    print(key)  # just prints the key
    print(programming_dictionary[key])  # I passed in the key, so it gives the value

# wipe existing dictionary
programming_dictionary = {}
print(programming_dictionary)
