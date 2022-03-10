
# TITLE
# A STRING METHOD
# .title()
# The first letter is capitalized in each word.

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("DanIEL", "LAngleY")
print(formatted_string)
# Output: Daniel Langley
