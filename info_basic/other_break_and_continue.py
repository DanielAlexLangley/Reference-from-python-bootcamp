
# BREAK
# This keyword allows you to break free of the loop. You can use it in a for or while loop.

scores = [34, 67, 99, 105]
for s in scores:
    if s > 100:
        print("Invalid")
        break
    print(s)


# CONTINUE
# This keyword allows you to skip this iteration of the loop and go to the next.
# The loop will still continue, but it will start from the top.

n = 1
while n < 100:
    if n % 2 == 0:
        continue
    print(n)
# Prints all the odd numbers
