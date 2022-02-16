text = '''
Slicing:

(All of this works for tuples, too.)

If you have a list, you can slice out a portion of it, like:
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])
Would give you cde

If you want to slice to the end of the list:
print(piano_keys[2:])

If you want to get everything up to position 5:
print(piano_keys[:5])

Set a third number to set the increment. 2 would give every other item.
print(piano_keys[2:5:2])
Would return ['c', 'e']

print(piano_keys[::2])
Would give every second item.
Would return ['a', 'c', 'e', 'g']

print(piano_keys[::-1])
Will reverse the list, going right from end to beginning.
g to a

Tuples:
piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti")
print(piano_tuple[2:5]
('mi', 'fa', 'so')
'''
