
# Scope
# this concept doesn't just apply to variables
# also applies to anything else you can name like functions

# Namespace
# anything you give a name to has a namespace, and that namespace is valid in certain scopes
# like if you define a function within another function, then that local function would be local to it


# this "enemies" is a global variable - is available within functions and outside functions
enemies = 1
def increase_enemies():
    # this "enemies" is a local variable - it is only valid within this function
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope EXAMPLE
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
# print(potion_strength) # this line of code will not work, since it was never defined as a global variable.
