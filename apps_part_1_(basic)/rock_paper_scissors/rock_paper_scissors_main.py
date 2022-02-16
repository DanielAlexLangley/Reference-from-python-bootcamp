
# example of random
# example of import
# rock, paper, scissors

from rock_paper_scissors_art import scissors
from rock_paper_scissors_art import paper
from rock_paper_scissors_art import rock
import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])
print("Computer chose:")
comp_choice = random.randint(0, 2)
print(game_images[comp_choice])
if int(user_choice) == comp_choice:
    print("Draw.")
elif (int(user_choice) == 2 and comp_choice == 1) or (int(user_choice) == 1 and comp_choice == 0) \
        or (int(user_choice) == 0 and comp_choice == 2):
    print("You win.")
else:
    print("You lose.")
