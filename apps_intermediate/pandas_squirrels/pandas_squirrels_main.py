
# Use csv and pandas to create csv called squirrel_count.csv...
# ...that has Fur Color and Count (of squirrels with that fur color)
# How many gray squirrels, how many cinnamon squirrels, how many black squirrels (from Primary Fur Color column)?
# Build new dataframe from it to make final csv

import pandas

data = pandas.read_csv("pandas_squirrels_2018_data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
