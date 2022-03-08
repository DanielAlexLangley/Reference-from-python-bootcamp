
# Global Constants
# the naming convention in python for global constants is to make them ALL UPPERCASE
# these are variables you define, and you're never planning on changing it ever again, like...


PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"


# Global Scope EXAMPLE:
player_health = 10
def game():
    def drink_potion():
        print(player_health)
    drink_potion()
print(player_health)


# "global" tag
# this imports a global variable into a function
# it is good practice to avoid modifying global scope within function, since it commonly causes problems
# instead, try to return outputs
enemies = 1  # global variable
def increase_enemies():
    global enemies
    enemies = 2  # would be a local variable, but we imported it with "global enemies"
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")


# Modifying Global Scope
# This is an example of how to properly modify a global variable
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
