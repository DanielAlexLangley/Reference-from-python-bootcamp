
# ITERROWS
# How to loop through a dataframe

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# pandas has an inbuilt loop, called ITERROWS
# Allows us to loop through rows rather than columns.
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)

# SEE NATO ALPHABET APP FOR BETTER EXAMPLE
