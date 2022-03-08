
# DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for item in list}
# Create a new dictionary based on values in existing dictionary:
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

print("Intro exercises:")
# Create a dictionary that generates a random score for each student in the list.
# The student name as a string will be the key, and the score as an int will be the value.
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# Use dictionary above to create dictionary "students_with_passing_score" that looks through dictionary above...
# ...anyone who has score 60 or over has passed. Everyone else failed.
students_with_passing_score = {student: score for (student, score) in students_scores.items() if score >= 60}
print(students_with_passing_score)
print("\n")

print("Exercise 1:")
# Create a dictionary called result that takes each word in the given sentence...
# ...and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Example Output:
# example = {
#     'What': 4,
#     'is': 2,
#     'the': 3,
#     'Airspeed': 8,
#     'Velocity': 8,
#     'of': 2,
#     'an': 2,
#     'Unladen': 7,
#     'Swallow?': 8
# }
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above. Write your code below:
result = {word: len(word) for word in sentence.split()}
print(result)
print("\n")

print("Exercise 2:")
# Create a dictionary called weather_f that takes each temperature in degrees Celsius...
# ...and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f: (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# Example_Output = {
#     'Monday': 53.6,
#     'Tuesday': 57.2,
#     'Wednesday': 59.0,
#     'Thursday': 57.2,
#     'Friday': 69.8,
#     'Saturday': 71.6,
#     'Sunday': 75.2
# }
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# Don't change code above. Write your code below:
weather_f = {day: ((temp_c * (9/5)) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)
print("\n")
