len("This is a type that this function accepts.")

# This is considered 'Type-Checking' 
print(type("Test Type 1"))
print(type(123.35))
print(type(123))
print(type(True))

# This is considered a 'Type-Conversion'
# User input is considered a string data type. We have to convert user input to numerical data types to do Math
# Len returns an integer, which cannot be concatenated in a string
print("Number of letters in your name: " + str(len(input("Enter your name: "))))