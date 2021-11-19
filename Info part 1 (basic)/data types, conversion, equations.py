

# order of operations is "PEMDAS"
pemdas = '''
go from left to right:
1st: parentheses
2nd: exponents
3rd: multiply, division
4th: add, subtract
'''
print(pemdas)


# data type is integer (whole number)
print(123 + 345)


# data type is floating point number (number with a decimal)
pi = 3.14159
print(pi)


# data type is boolean (only true or false)
# first letter is always capital letter
one = True
two = False
if True:
    print("It's true!")


# use underscores for commas rather than commas
# (these underscores will not show up when printing. they only help in the code.)
print(123_456)


# type check of variable
num_char = len(input("What is your name? "))
print(type(num_char))


# Convert into a string
num_char2 = len(input("What is your name? "))
new_num_char = str(num_char2)
print("Your name has " + new_num_char + " characters.")


# Convert into integer
a = int("3")
print(type(a))


# Convert into a float
b = 123
print(type(b))
c = float(b)
print(type(c))


# example of conversion:
age = input("What is your current age? ")
print(f"You have {365 * (90 - int(age))} days, {52 * (90 - int(age))} weeks, and {12 * (90 - int(age))} months left.")


# equations
n = 0
n += 2     # use + to add
print(n)
n -= 1     # use - to subtract
print(n)
n *= 6     # use * to multiply
print(n)
n /= 3     # use / to divide
print(n)   # division always gives float data type
m = 3 ** 3 # use ** for exponents aka power, like 2 ** 3 which is 2x2x2 = 8
print(m)


# if you want int data type from division no matter what, use floor division
print(8 // 3)


# rounds to all decimals unless you tell it where to cut it off at which is the "2" below in the second example
# if you just do round(8 / 3) then I think it defaults to rounding to the nearest whole number
print(round(8 / 3))
print(round(8 / 3, 2))

