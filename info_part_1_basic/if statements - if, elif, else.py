
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
