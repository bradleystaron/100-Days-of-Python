programming_dictionary = {
    "Bug": "Indentation Error",
    "Function": "An action that can be called over and over again",
    "Loop": "The action of doing something over and over again"

}

print(programming_dictionary["Bug"])

programming_dictionary["Return Type"] = "This assigns the definition of Return Type"

print(programming_dictionary)

empty_dictionary = {}

# Wiping an existing dictionary

# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)


# How to loop through a dictionary
for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])