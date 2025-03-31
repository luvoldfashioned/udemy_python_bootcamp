# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))

# # data_dict = data.to_dict()
# # print(data_dict)

# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Rows
# print(data[data.day == "Monday"])

# # Print the row of data which had the highest temperature.
# print(data[data.temp == data.temp.max()])

# # Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 1.8 + 32
# print(monday_temp_F)

# Create a Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
