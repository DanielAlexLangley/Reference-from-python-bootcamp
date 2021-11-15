

# comparisons
# = assigns the value
# == comparison that checks if equal to
# != comparison that checks if it is not equal to


# if, elif, else
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


# nested:
c = 2
d = 1
if c != d:
    if c > d:
        print("This is an example of nested if statement.")


# logical operators
# and, or, not
e = 1
f = 2
if e < f and e + f == 3:
    print("Success!")
wants_photo = input("Do you want a photo taken? Y or N. ")
if wants_photo == "Y":
    print("Second success!")


# modulo is the operator %
# modulus is the number on the right side of the equation (the n2 in the below example)
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
m1 = n1 % n2
print(m1)


