# with open("weather_data.csv") as weather_data:
#     lst=weather_data.readlines()
#     print(lst)

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures =[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

# Get the average of temperatures
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))

# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp*1.8 + 32)