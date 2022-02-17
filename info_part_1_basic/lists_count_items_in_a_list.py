
# count number of items in a list

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number = len(names)
print(number)
random_name = random.randint(0, number - 1)
print(f"{names[random_name]} is going to buy the meal today!")
