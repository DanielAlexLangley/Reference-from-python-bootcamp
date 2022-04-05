
# example
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(((total / split) * ((tip / 100) + 1)), 2)}")

# If you want the final_amount to always have 2 decimal places.
# e.g. $12 becomes $12.00
# You can use this link to figure out how to do this:
# https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
# This is how you can implement it:

bill_per_person = round(((total / split) * ((tip / 100) + 1)), 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

