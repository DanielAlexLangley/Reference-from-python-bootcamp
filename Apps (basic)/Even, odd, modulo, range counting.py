

# is it odd or even
# method 1
odd_even_number = int(input("Which number do you want to check if it is odd or even? "))
if odd_even_number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# method 2 (code goal is to add up all the even numbers from 1 to 100)
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)


# method 3 (code goal is to add up all the even numbers from 1 to 100)
even_sum = 0
for number in range(2, 101, 2):
    # print(number)
    even_sum += number
print(even_sum)

