
# for loop with list
# can't use SUM() function in this example
# can't use LEN() function in this example
# enter heights like this: 20 30 40 50 60 70
student_heights = input("Input a list of student heights: ").split()
print(student_heights)
for n in range(0, len(student_heights)):
    # this for loop converts each string into an integer
    student_heights[n] = int(student_heights[n])
print(student_heights)
# the above code was given in the assignment and should not be changed
total = 0
heights = 0
for height in student_heights:
    heights += height # this adds up each height item
    total += 1 # this line counts the number of height items
print(round(heights / total)) # this divides the total height by the number of height items, to give the average height
print("\n")


# calculate the highest score from a list of scores
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# can't use max() or min() which would give you the max or min of the list inside the ()
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score in the class is: {highest}")
