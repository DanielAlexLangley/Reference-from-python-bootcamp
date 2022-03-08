
# split string into list

import random_info

names_string = input("Give me everybody's names, separated by a comma and a space: ")  # type is string
names = names_string.split(", ")                                           # type is list
print(names)
random_name = random.choice(names)                                         # type is string
print(random_name + " is going to buy the meal today!")
