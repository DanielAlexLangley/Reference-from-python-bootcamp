

# for item in list:
# do something to each item


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    # doing this assigns a variable to the string in the list.
    # the first time it runs, the string is apple, 2nd time peach, etc
    print(fruit + " Pie")
print("\n")

# for number in range(a, b):
# print(number)
# it starts on a
# it stops on b, so if you want it to display 10, you have to type 11
for number in range(1, 11):
    print(number)
print("\n")


# it normally counts up by 1, but if you want it to count up higher, you can add a step after b
# for number in range(a, b, c):
# print(number)
for number in range(1, 11, 3):
    print(number)
print("\n")


# if range just has input instead of two:
# it assumes the first input is integer 0, then the actual input is the high number it stops on
total = 0
for number in range(10):
    print(number)
print("\n")


# another example
total = 0
for number in range(1, 101):
    total += number
print(total)
print("\n")


# for loop with list
# can't use SUM() function in this example
# can't use LEN() function in this example
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
heights = 0
for height in student_heights:
    heights += height
    total += 1
print(round(heights / total))
print("\n")


# calculate the highest score from a list of scores
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# can't use max() or min() which would give you the max or min of the list inside the ()
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score in the class is: {highest}")
print("\n")

