

# other stuff you can do with lists:
# https://docs.python.org/3/tutorial/datastructures.html


# create a list
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
    "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
    "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
    "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# lists can be printed
print(states_of_america)


# access just one item in the list
print(states_of_america[0])


# count from the end of the list aka "negative index"
print(states_of_america[-1])


# change item in the list
states_of_america[0] = "Pants"
print(states_of_america[0])


# add item to end of the list
states_of_america.append("Last state")
print(states_of_america)


# add items to end of the list
states_of_america.extend(["State52", "State53"])
print(states_of_america)


# lists can be combined into a list variable
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen1 = [fruits, vegetables]
print(dirty_dozen1)


# list[][]
dirty_dozen2 = [
    "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
    "Celery", "Potatoes"]
print(dirty_dozen2[1][0])
print(dirty_dozen2[1][1])
print(dirty_dozen2[1][2])
print(dirty_dozen2[1][3])
print(dirty_dozen2[1][4])
print(dirty_dozen2[1][5])


# split string into list
import random
names_string = input("Give me everybody's names, separated by a comma. ")  # type is string
names = names_string.split(", ")                                           # type is list
random_name = random.choice(names)                                         # type is string
print(random_name + " is going to buy the meal today!")


# count in a list
# import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number = len(names)
random_name = random.randint(0, number - 1)
print(f"{names[random_name]} is going to buy the meal today!")

