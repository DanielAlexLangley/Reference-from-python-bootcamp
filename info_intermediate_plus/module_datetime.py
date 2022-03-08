
import datetime

print("Example 1:")
now = datetime.datetime.now()
print(type(now))
print(now)

print("Example 2:")
year = now.year
print(type(year))
print(year)

print("Example 3:")
day_of_week = now.weekday()
print(day_of_week)  # Monday is 0, Tuesday is 1, etc.

print("Example 4:")
date_of_birth = datetime.datetime(year=1980, month=1, day=1)
print(date_of_birth)

