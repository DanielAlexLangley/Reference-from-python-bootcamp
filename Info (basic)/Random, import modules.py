

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


random_side = random.randint(0,1)
if random_side == 0:
    print("Tails")
else:
    print("Heads")


random_integer = random.randint(1, 10)
print(random_integer)
# 0.00000000 - 0.99999999...
random_float = random.random()
print(random_float)
# how to combine the above two?
# my method I came up with:
random_combined = random.randint(0, 5) + random.random()
print(random_combined)
# teacher's method:
print(random_float * 5)


# import a module
# example of using random
# rock, paper, scissors
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])
print("Computer chose:")
comp_choice = random.randint(0,2)
print(game_images[comp_choice])
if int(user_choice) == comp_choice:
    print("Draw.")
elif (int(user_choice) == 2 and comp_choice == 1) or (int(user_choice) == 1 and comp_choice == 0) \
        or (int(user_choice) == 0 and comp_choice == 2):
    print("You win.")
else:
    print("You lose.")


# import just a portion
# from pi import pie
# print(pie)


