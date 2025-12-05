# This Program acts as an even or odd number calculator

UserInput = int(input("What is your number? "))

# If the divided number is a clean division with zero remaining, then it is even, otherwise it is odd
if UserInput % 2 == 0:
    print(f"{UserInput} is even.")
else: 
    print(f"{UserInput} is odd.")