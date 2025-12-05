capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# Prints the value at the first index of France
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"] 
    },
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"]["cities_visited"][2])