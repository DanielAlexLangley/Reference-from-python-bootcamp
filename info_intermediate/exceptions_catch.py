
# CATCH EXCEPTIONS (4 keywords)
# RAISE OUR OWN EXCEPTIONS (1 keyword)

# If an error happens like a file not found error, or key error, or index error, or type error...
# Then so far in this class, our program has just failed and ended.
# In real life, you plan for these failures, by trying to catch these exceptions,
# so that our program doesn't have to totally fail.

# try
# except
# else
# finally

# These are the four keywords when trying to catch an exception.

# Use "try" first as the code you want to run but that might cause an exception to happen.
# Use "except" second which is the code you want to run only if the exception happened.
# Use "else" third which is the code that will run if there were no exceptions.
# Use "finally" fourth which is the code to run no matter what happens (whether "try" code failed or succeeded).

# For "except" you should limit it to certain exceptions, like "except FileNotFoundError"
# So you can have multiple exceptions. Like also have "except KeyError"

# If you catch an exception, but you still want to get a hold of that error message,
# use "except KeyError as error_message:"
# That puts the error message in the strong error_message, and you can say,
# print(f"The key {error_message} does not exist.")

# "Finally" is not often used.

# The fifth keyword is "raise".
# If you type "raise KeyError" then it will raise a key error no matter what.
# "raise TypeError("Message") which will display your message too.
# When would you want to raise your own error?
# Like if the user enters a value that doesn't make sense, use...
# if entered_value > 4:
# raise ValueError("Value should be between 0 and 4")
# which will give error that value entered is probably wrong, like if they put in 5.

print("Exercise 1: ")
fruits = ["Apple", "Pear", "Orange"]
# Catch the exception and make sure the code runs without crashing.
# If the user enters something that is out of range just print a default output of "Fruit pie".
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
make_pie(4)

print("Exercise 2: ")
# The code will crash and give you a KeyError.
# This is because some posts in the facebook_posts don't have any "Likes".
# Use exception handling to prevent crashing.
# If a post has no likes, treat it like 0 likes.
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
print(total_likes)

print("Exercise 3: ")
import pandas
data = pandas.read_csv("../apps_intermediate/pandas_nato/pandas_nato_phonetic.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()
