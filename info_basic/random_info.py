
# example of random
# example of import

import random

random_side = random.randint(0, 1)
if random_side == 0:
    print("Tails")
else:
    print("Heads")

# pick a random int from 0, 1, 2, or 3
random_integer = random.randint(0, 3)
print(random_integer)

# pick a random floating point number:
# use .random() and it will return random floating point number between:
# 0.00000000 - 0.99999999...
random_float = random.random()
print(random_float)

# what if you wanted a random floating point number between 0 and 5?
# method 1 (that I came up with)
random_combined = random.randint(0, 4) + random.random()
print(random_combined)
# method 2 (that teacher came up with):
print(random_float * 5)
