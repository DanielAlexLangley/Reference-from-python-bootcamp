
# TO DO: Create a letter using file_paths_main_merge_starting_letter.txt
# for each name in file_paths_main_merge_invited_names.txt
# replace the [name] placeholder with the actual name.
# Save the letters in the folder "file_paths_mail_merge_readytosend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("file_paths_mail_merge_input/file_paths_mail_merge_names/file_paths_main_merge_invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("file_paths_mail_merge_input/file_paths_mail_merge_letters/file_paths_main_merge_starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open(f"mail_merge_output/file_paths_mail_merge_readytosend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
