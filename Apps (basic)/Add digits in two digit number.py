

# program that adds the digits in a 2 digit number.
# this is subscripting


# best method
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# alternative method:
two_digit_number2 = input("Type a two digit number: ")
str_first_number = two_digit_number2[0]
str_second_number = two_digit_number2[1]
print(int(str_first_number) + int(str_second_number))

