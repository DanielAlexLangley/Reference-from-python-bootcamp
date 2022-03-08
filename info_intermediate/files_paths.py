
# "Absolute file path" is always relative to the root (which is C drive).
# Example of absolute path:
# C:\MyBackupCtoG\PycharmProjects\reference_from_python_bootcamp\main.py
#
# "Working directory" is the folder we're currently working from.
# "Relative file path" is relative to the working directory.
# Like if the working directory was PycharmProjects, then the relative file path would be:
# ./reference_from_python_bootcamp/main.py
#
# (Even on Windows it's correct to use forward rather than backslashes, even though Windows uses backslashes.)
#
# What if your working folder was reference_from_python_bootcamp, but you needed a file from PycharmProjects?
# Use two dots.
# Two dots represents going up one step in the hierarchy to the parent folder.
# ../
#
# If the file you need is in the working folder, then you just write:
# ./file_name.doc
# Or you can omit the ./ if it's just ./ since it would just bring you back into the same folder you left from.
#
# Like if a file was on the desktop, it would be
# "/Users/Daniel/Desktop/file_name.txt"
# So you don't write the C: part.
#
# So if I wanted to go from my working folder for this file (which is "files_paths.py"):
# C:\MyBackupCtoG\PycharmProjects\reference_from_python_bootcamp\info_intermediate
# To:
# C:\Users\Daniel\Desktop\MyStuff
# It would be:
# "../../../../Users/Daniel/Desktop/MyStuff
# Each of the ../ takes me up one folder from the working folder, then once you have as many of those as you need,
# You can go back down to the folder you need to get to.
#
# After you type the ../, Pycharm is smart enough that it will start making suggestions of folders that are available
# going back down the chain.


with open("../../../../Users/Daniel/Desktop/MyStuff/test.txt") as file:
    pass

# See file_paths_mail_merge program for example.
