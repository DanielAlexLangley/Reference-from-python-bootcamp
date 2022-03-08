

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
# -1 is the last item in the list
# -2 is the second to last item in the list
print(states_of_america[-1])
print(states_of_america[-2])


# change item in the list
states_of_america[0] = "First"
print(states_of_america[0])


# add item to end of the list
states_of_america.append("State51")
print(states_of_america)


# add items to end of the list
states_of_america.extend(["State52", "State53"])
print(states_of_america)


# example
number_of_states = len(states_of_america)
print(states_of_america[number_of_states - 1])
