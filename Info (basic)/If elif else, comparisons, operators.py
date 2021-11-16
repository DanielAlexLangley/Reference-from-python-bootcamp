

# comparisons
# = assigns the value
# == comparison that checks if equal to
# != comparison that checks if it is not equal to


# if, elif, else
print("\n")
a = input("Type the first number: ")
b = input("Type the second number: ")
if a > b:
    print("First number is greater than the second number.")
elif b > a:
    print("Second number is greater than the first number.")
elif a == b:
    print("The numbers are equal.")
else:
    print("Something else happened.")
print("\n")


# nested:
c = 2
d = 1
if c != d:
    if c > d:
        print("This is an example of nested if statement.")
print("\n")


# logical operators
# and, or, not
e = 1
f = 2
if e < f and e + f == 3:
    print("Success!")
wants_photo = input("Do you want a photo taken? Y or N. ")
if wants_photo == "Y":
    print("Second success!")
print("\n")


# Treasure map
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
treasure_map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

