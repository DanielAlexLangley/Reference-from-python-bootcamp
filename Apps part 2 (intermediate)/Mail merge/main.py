# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

new_list = []

names = open("./Input/Names/invited_names.txt")
names_list = names.readlines()
for _ in names_list:
    new_name = _.strip("\n")
    new_list.append(new_name)
names.close()

for this_name in new_list:
    letter = open("./Input/Letters/starting_letter.txt")
    starting_letter = letter.readlines()
    starting_letter[0] = starting_letter[0].replace("[name]", this_name)
    name = starting_letter[0].strip("\n")
    file = open(f"./Output/ReadyToSend/{name}.txt", mode="a")
    for _ in starting_letter:
        file.write(_)
    file.close()
    letter.close()
