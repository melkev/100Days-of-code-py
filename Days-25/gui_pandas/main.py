# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")


temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp)

celsius = int(monday.temp)
fahrenheit = 9.0/5.0 * celsius + 32
print(fahrenheit)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Julia", "carla"],
    "scores": [76, 56, 65]
}

data_new = pandas.DataFrame(data_dict)
data_new.to_csv("new_data.csv")
