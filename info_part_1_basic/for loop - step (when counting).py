
# it normally counts up by 1, but if you want it to count up higher, you can add a step after b
# for number in range(a, b, c):
# print(number)

total = 0
for number in range(2, 101, 2):
    total += number
print(total)
