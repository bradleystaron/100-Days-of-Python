print("Welcome to the rollercoaster")

height = int(input("What is your height? "))

if height >= 120:

    age = int(input("How old are you? "))

    if age >= 16:
        print("Please pay $10.")
    elif age < 16 or age > 12:
        print("Please pay $5.")
    else:
        print("Please pay $3.")

else:
    print("You aren't tall enough to ride.")