
from prettytable import PrettyTable

text = '''

https://pypi.org/project/prettytable/
Helps us display tables in ascii format.
Click the link to find out more about it:
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

'''

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"  # change attribute to left aligned
print(table)
