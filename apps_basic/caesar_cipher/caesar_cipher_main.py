
# see below for a great example of a modulo

# INDEX INDEX INDEX INDEX INDEX
# https://www.w3schools.com/python/ref_list_index.asp

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

from caesar_cipher_alphabet import alphabet
from caesar_cipher_logo import logo


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)
end_cypher = False
while not end_cypher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # great example of the use of modulo:
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        end_cypher = True
        print("Goodbye!")
