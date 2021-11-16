# make our own function

# def means to create/define the function we're going to make
# my_function is the name of my function I'm going to make
# everything that comes after the : will be what the function does
def my_function():
    print("Hello")
    print("Bye")


# to "call" AKA execute the function, write the function name...
# ...plus any necessary inputs (which is what goes in the parenthesis)
my_function()


# while loop:
# while variable_name_is_true:
#     do this thing repeatedly

# reeborg's world
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
#
# def turn_around():
#     turn_left()
#     turn_left()
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def walk_square():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#
# walk_square()


# reeborg's challenge 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for number in range(0, 6):
#     jump()


# reeborg's challenge 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# use previous code from challenge 1, plus:
# while at_goal() != True:
#     jump()
#
# can also write:
# while not at_goal():
#     jump()


# reeborg's challenge 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#
# plus I had to change the jump function


# reeborg's challenge 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     else:
#         turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# reeborg's maze challenge
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# she provided 3 zip files that had mazes where he was stuck in the beginning in a tough spot. my code for those 3:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not wall_on_right():
#     if not wall_on_right():
#         turn_right()
#         if not wall_on_right():
#             turn_right()
#             if not wall_on_right():
#                 turn_right()
#                 if not wall_on_right():
#                     turn_right()
#                     move()
#
# while not at_goal():
#     if wall_on_right() and front_is_clear():
#         move()
#     elif wall_on_right() and not front_is_clear():
#         turn_left()
#     elif not wall_on_right():
#         turn_right()
#         move()
#
#
# in her example solution, she just had him walk forward until he hit a wall,
# then turn right, then go to the rest of the code.
# i didn't do it like that since I thought he was always supposed to try to grab the right wall
