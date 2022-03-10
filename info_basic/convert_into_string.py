
# CONVERT INTO A STRING

num_of_characters = len(input("What is your name? "))
# Input: Daniel
print(type(num_of_characters))
# Output: <class 'int'>

new_num_of_characters = str(num_of_characters)
print(type(new_num_of_characters))
# Output: <class 'str'>

print("Your name has " + new_num_of_characters + " characters.")
# Output: Your name has 6 characters.
