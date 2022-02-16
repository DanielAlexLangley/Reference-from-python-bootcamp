
# modulo
# goal is to add up all the even numbers from 1 to 100
# method 1

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)


# method 2

even_sum = 0
for number in range(2, 101, 2):
    # print(number)
    even_sum += number
print(even_sum)
