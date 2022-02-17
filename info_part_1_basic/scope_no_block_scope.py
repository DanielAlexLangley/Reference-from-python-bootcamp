
# no block scope

# There is no block scope in python
# if block, while loop, for loop, or any block of code that is indented, any variable in this will have...
# ...the same scope as enclosing function, # or if no enclosing function then scope is global.

if 3 > 2:
    a_variable = 10  # this is a variable created inside a block of code
print(a_variable)  # this works and prints since there is no block scope in python, therefore this is a global variable


# There is no Block Scope EXAMPLE:
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)
# print(new_enemy) # this line of code won't work, since "new_enemy" is local to the function
create_enemy()
