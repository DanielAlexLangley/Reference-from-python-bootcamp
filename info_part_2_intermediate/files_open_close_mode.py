
# FILES
# OPENING FILES
# CLOSING FILES
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# To open a file:
file = open("../../../../Users/Daniel/Desktop/my_desktop_test_file.txt", mode="w")
# The "open" command is built into Python, so we don't need to import it to use it.
# If you try to open a file (in write mode only?), and if that file doesn't exist, it will make that file for you.
# Once you open a text file, you can save the contents as a string and do other things.
# When you're done with the file, you need to close the file to free up the resources it was using on your computer.
# With the open command, one of the parameters is mode, and the default is read only, so change it to "w" for write.
# To write, use write command.
file.write("Line 1.")
file.close()
print(file)

# Since it can be hard to remember to close the file, some programmers use the "with" "as" keywords instead of "open".
# If you use "with", it will close it down for you when it's done.
# Writing to it will delete the current text and write the new text.
# If you want to write to it but not delete the current text, append by using "a" instead of "w":
with open("../../../../Users/Daniel/Desktop/my_desktop_test_file.txt", mode="a") as file:  # The word "file" is...
    # ... a variable. You can name it anything. It doesn't have to be called "file".
    file.write("\nLine 2.")
    print(file)


with open("../../../../Users/Daniel/Desktop/my_desktop_test_file.txt", mode="a") as file:
    file.write("\nLine 3.")
    print(file)

with open("../../../../Users/Daniel/Desktop/my_desktop_test_file.txt") as file:
    contents = file.read()  # this .read() saves it as a string, not as a list.
    print(type(contents))
    print(contents)
