
# Convert csv into dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# Create a list of the phonetic code words from a word that the user inputs.
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

new_dict = {}
data = pandas.read_csv("nato_alphabet_phonetic.csv")
for (index, row) in data.iterrows():
    new_dict[row.letter] = row.code
print(new_dict)
word = input("Enter a word: ").upper()
output_list = [new_dict[letter] for letter in word]
print(output_list)
