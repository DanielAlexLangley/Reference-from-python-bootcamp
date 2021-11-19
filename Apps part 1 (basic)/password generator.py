

import random
letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Password Generator Project
# this version randomizes a list
print("\n")
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
password1 = ""
for char in password_list:
    password1 += char
print(f"Your password is: {password1}")


# Password Generator Project
# this version randomizes a string
print("\n")
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_nr = ""
for letter in range(1, nr_letters + 1):
    letter_rd = random.choice(letters)
    password_nr += letter_rd
for letter in range(1, nr_symbols + 1):
    symbol_rd = random.choice(symbols)
    password_nr += symbol_rd
for letter in range(1, nr_numbers + 1):
    number_rd = random.choice(numbers)
    password_nr += number_rd
print(password_nr)
password2 = ''.join(random.sample(password_nr, len(password_nr)))
print(password2)
