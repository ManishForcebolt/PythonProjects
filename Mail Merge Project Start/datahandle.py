import pandas
import numpy as np

squirrel_data = pandas.read_csv("/Users/ca/Desktop/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data.head())
# print(squirrel_data.columns)
# print(squirrel_data.describe())

grey_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

print(len(grey_squirrel))
print(len(cinnamon_squirrel))
print(len(black_squirrel))

