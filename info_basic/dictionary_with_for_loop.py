
# DICTIONARIES
# USE A FOR LOOP TO CHANGE THE VALUE OF EACH KEY

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
# Output:
# {
#     'Harry': 'Exceeds Expectations',
#     'Ron': 'Acceptable',
#     'Hermione': 'Outstanding',
#     'Draco': 'Acceptable',
#     'Neville': 'Fail'
# }
