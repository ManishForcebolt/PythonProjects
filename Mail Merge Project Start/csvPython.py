# with open("weather_data.csv") as csvfile:
#     data = csvfile.readlines()
#     print(data)
import pandas
# import pandas as pd
# import numpy as np
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperature = []
#     day = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         if row[0] != "day":
#             day.append(row[0])
# print(day)
# print(temperature)
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
# temp_list.append(22)  # To add more element

print(f"After append\n{temp_list}")
print(data.columns[2])
# Average of Temperature
# temp_avg = sum(temp_list)/len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data["temp"].mode())

data = pandas.read_csv("weather_data.csv")

# Accessing columns
temp = data["temp"].to_list  # having as list
print(temp)
print(data.condition)

# Accessing row of dataframe
# row = data[data.temp == data.temp.min()]
# print(data[data.temp == 12])
# print(row)
# print(type(row))
# print(row["day"])

# Creating new data file using dictionary data structure
data_dict = {
    "name": ["Kartik", "Manas", "Yashika", "Sundar", "Sweeti"],
    "gender": ["M", "M", "F", "M", "F"]
}

data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("new_data.csv")


