text1 = '''

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

The "open" command is built into Python, so we don't need to import it to use it.

Once you open a text file, you can save the contents as a string and do other things.

When you're done with the file, you need to close the file to free up the resources it was using on your computer.

Since it can be hard to remember to close the file, some programmers use the "with" keyword instead of "open".

If you use "with", it will close it down for you when it's done.

To write, use write command.
But with the open command, one of the parameters is mode, and the default is read only.
So change it to "w" for write.
Writing to it will delete the current text and write the new text.

If you want to write to it but not delete the current text, use "a" instead of "w".
"a" stands for append.

If you try to open a file in write mode, and if that file doesn't exist, it will make that file for you.

'''

file = open("my_text.txt", mode="w")
# contents = file.read()
file.write("Line 1.")
file.close()
print(file)

# "word" in the line below is a variable that you can name whatever you want the variable named.
with open("my_text.txt", mode="a") as file:
    # contents = file.read()
    file.write("\nLine 2.")
    print(file)

text2 = '''

"Absolute file path" is always relative to the root (which is C drive).
Like:
C:\MyBackupCtoG\PycharmProjects\Reference-from-python-bootcamp\main.py

"Working directory" is the folder we're currently working from.
"Relative file path" is relative to the working directory.
Like if the working directory was PycharmProjects, then the relative file path would be:
./Reference-from-python-bootcamp/main.py

(Even on Windows it's correct to use forward rather than backslashes, even though Windows uses backslashes.)

What if your working folder was Reference-from-python-bootcamp but you needed a file from PycharmProjects?
Use two dots.
Two dots represents going up one step in the hierarchy to the parent folder.
../

If the file you need is in the working folder, then you just write:
./file_name.doc
Or you can omit the ./ if it's just ./ since it would just bring you back into the same folder you left from.

Like if a file was on the desktop, it would be
"/Users/Daniel/Desktop/file_name.txt"
So you don't write the C: part.

So if I wanted to go from my working folder of:
C:\MyBackupCtoG\PycharmProjects\Reference-from-python-bootcamp
To:
C:\Users\Daniel\Desktop\MyStuff
It would be:
"../../../../Users/Daniel/Desktop/MyStuff
Each of the ../ takes me up one folder from the working folder, then once you have as many of those as you need,
You can go back down to the folder you need to get to.

After you type the ../, Pycharm is smart enough that it will start making suggestions of folders that are available
going back down the chain.

'''

# with open("../../../../Users/Daniel/Desktop/MyStuff/test.txt") as file:
#     pass

# See Mail merge program for example.
