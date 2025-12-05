#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n")) 
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

# Creates a blank list to put the elements in
blank_list = []

# Appends letters to blank_list
for letter in range(0, number_letters):
    random_element = random.choice(letters)
    blank_list.append(random_element)

# Appends symbols to blank_list
for symbol in range(0, number_symbols):
    random_element = random.choice(symbols)
    blank_list.append(random_element)

# Appends numbers to blank_list
for number in range(0, number_numbers):
    random_element = random.choice(numbers)
    blank_list.append(random_element)

# Prints out the blank list not randomized
print(blank_list)

# Prints out the blank list randomized
random.shuffle(blank_list)
print(blank_list)

# Joins all of the individual characters in each element into one string 
list_as_string = "".join(blank_list)

# Prints out the final password as a list
print(f"Your password is {list_as_string}")
