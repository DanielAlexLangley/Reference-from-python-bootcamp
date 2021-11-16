

# modulo is the operator %
# modulus is the number on the right side of the equation (the n2 in the below example)
print("\n")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
m1 = n1 % n2
print(m1)
print("\n")


# Fizz Buzz game:
# if divisible by 3, fizz
# if divisible by 5, buzz
# if divisible by both, fizzbuzz
print("start")
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
print("\n")


# is a year a leap year?
# leap year is:
# every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
year = int(input("Which year do you want to check? "))
if year % 4 != 0:
    print("Not leap year.")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
print("\n")


# is it odd or even
# method 1
odd_even_number = int(input("Which number do you want to check if it is odd or even? "))
if odd_even_number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
print("\n")


# is it odd or even
# method 2 (code goal is to add up all the even numbers from 1 to 100)
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
print("\n")


# is it odd or even
# method 3 (code goal is to add up all the even numbers from 1 to 100)
even_sum = 0
for number in range(2, 101, 2):
    # print(number)
    even_sum += number
print(even_sum)
print("\n")

