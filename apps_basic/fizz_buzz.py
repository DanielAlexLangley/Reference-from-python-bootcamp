
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
