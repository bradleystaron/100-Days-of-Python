# # import csv

# # # Opens weather data file and creates a list named data that contains the values from the file
# # with open("100_Days_of_Code_Python/Days_22-25/Day25_ActiveExamples/weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas

# data = pandas.read_csv("100_Days_of_Code_Python/Days_22-25/Day25_ActiveExamples/weather_data.csv")
# # print(type(data))
# # print(data["temp"]) 

# data_dict = data.to_dict()
# print(data_dict)

# temperature_list = data["temp"].to_list()
# print(len(temperature_list))

# #calculate average temperature
# print(data["temp"].mean())
# average_temp = sum(temperature_list) / len(temperature_list)
# print(average_temp)

# # get data in a column
# print(data["condition"])
# print(data.condition)

# # get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# # Get Monday's condition
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # Convert Monday's temperature to Fahrenheit
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("100_Days_of_Code_Python/Days_22-25/Day25_ActiveExamples/new_data.csv")

import pandas
data = pandas.read_csv("100_Days_of_Code_Python/Days_22-25/Day25_ActiveExamples/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("100_Days_of_Code_Python/Days_22-25/Day25_ActiveExamples/squirrel_count.csv")
   