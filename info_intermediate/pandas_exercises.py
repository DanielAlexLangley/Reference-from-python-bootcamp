

print("Exercise 1:")
with open("pandas_weather_data.csv") as data_file:
    data = data_file.readlines()  # .readlines takes each line in the file and will turn it into an item in a list.
    print(type(data))
    print(data)
    print("\n")


import csv
print("Exercise 2:")
# But we don't just want a list with each line as an item,
# so we will import csv, so we can do more advanced things.
with open("pandas_weather_data.csv") as data_file:
    data = csv.reader(data_file)  # .reader made a csv reader object
    print(data)
    # this object can be looped through, so we can do:
    for row in data:
        print(row)
    print("\n")


print("Exercise 3:")
# make a list called temperatures that list each temperature item as an int, not a string
with open("pandas_weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    print("\n")


print("Exercise 4:")
import pandas
data = pandas.read_csv("pandas_weather_data.csv")
# There are many arguments that can go in the () for this, all of them optional except one.
# That one that is not optional is the path.
print(data)
print("\n")


print("Exercise 5:")
data = pandas.read_csv("pandas_weather_data.csv")
print(data["temp"])
print("\n")


print("Exercise 6:")
data = pandas.read_csv("pandas_weather_data.csv")
print(type(data))  # data type of "data" is a pandas DataFrame object.
# In the Pandas documentation, it talks about the two primary data structures of pandas: series, and dataframes.
# A dataframe is like one entire sheet of a spreadsheet.
print(type(data["temp"]))  # This datatype is a series.
# A series is like a list that is a single column in your table.
print("\n")


print("Exercise 7:")
data = pandas.read_csv("pandas_weather_data.csv")
data_dict = data.to_dict()
print(data_dict)
print("\n")


print("Exercise 8:")
data = pandas.read_csv("pandas_weather_data.csv")
temp_list = data["temp"].to_list()  # Converts column to a list.
print(temp_list)
# Find the average of the temperatures not using pandas
temp_average = sum(temp_list) / len(temp_list)
print(temp_average)
# Find average using pandas
print(data["temp"].mean())
# Find maximum value (from temperature column) using pandas
print(data["temp"].max())
print("\n")


print("Exercise 9:")
data = pandas.read_csv("pandas_weather_data.csv")
# Instead of typing data["temp"], you can just write data.temp
# Capital letters matter here. Must type it exactly, no matter which way you use.
print(data.condition)
print("\n")


print("Exercise 10:")
data = pandas.read_csv("pandas_weather_data.csv")
# Get data in the row:
print(data[data.day == "Monday"])
print("\n")


print("Exercise 11:")
data = pandas.read_csv("pandas_weather_data.csv")
# How to pull out row of data where temperature was at the maximum?
print(data[data.temp == data.temp.max()])
print("\n")


print("Exercise 12:")
data = pandas.read_csv("pandas_weather_data.csv")
# What if we want only one piece of info from a row? Such as just that row's temperature, or just that row's condition?
monday = data[data.day == "Monday"]
print(monday.condition)
print("\n")


print("Exercise 13:")
data = pandas.read_csv("pandas_weather_data.csv")
# Get Monday's temperature, but convert it to fahrenheit, since it's currently in celsius.
monday = data[data.day == "Monday"]
monday_temp_F = (int(monday.temp) * (9/5)) + 32
print(monday_temp_F)
print("\n")


print("Exercise 14:")
# Create a dataframe from scratch
# Let's say we have a dictionary with these values:
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# How to create dataframe from this dictionary?
data = pandas.DataFrame(data_dict)
print(data)
# How to convert that dataframe to csv file?
data.to_csv("../../../../Users/Daniel/Desktop/new_data.csv")
print("\n")
