
################### Scope ####################
#this concept doesn't just apply to variables
#also applies to anything else you can name like functions
#namespace:
#anything you give a name to has a namespace, and that namespace is valid in certain scopes
#like if you define a function within another fucntion, then that local function would be local to it

enemies = 1 #global - is available within functions and outside functions

def increase_enemies():
  enemies = 2 #local variable - only valid within this function
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")






################### no block scope ####################

#There is no block scope in python
#this is indented block of code. this variable has same scope as enclosing function, or if no enclosing function, then scope is global
if 3 > 2:
  a_variable = 10 #this is a variable created inside a block of code
print(a_variable) #this works and prints since there is no block scope in python


#global constants
#naming convention in python for these is to make them ALL UPPERCASE
#varibles you define and you're never planning on changing it ever again, like...
PI = 3.14159
URL = www.whatever.com


################### "global" tag ####################
#good practice to avoid modifying global scope within function, since it commonly causes problems
#instead, try to return outputs

enemies = 1 #global variable

def increase_enemies():
  global enemies
  enemies = 2    #would be a local variable but we imported it with "global enemies"
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")










################### Scope examples ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

