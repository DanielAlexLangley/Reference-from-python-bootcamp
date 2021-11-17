text = '''
Tuple is a data type in Python.
Each of the items that are in a tuple are ordered.
It's similar to a list.
A tuple looks like a list:
(1, 3, 7)
To make a tuple variable:
my_tuple = (1, 3, 8)
my_tuple[0] would bring up 1
my_tuple[2] would bring up 8
Why use tuple instead of list?
It is immutable.
That means a tuple is carved in stone.
You can't change the values like you can in a list.
If you wanted to do:
my_tuple[2] = 12
This will not work. It's a type error. You can't remove items, etc.
So you can use a tuple if you want to disallow others from changing it.
If you want to change it, convert it to a list.
'''
