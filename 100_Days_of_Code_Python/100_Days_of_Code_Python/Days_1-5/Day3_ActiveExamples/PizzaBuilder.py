print("Welcome to the Pizza Builder Program!")

size = input("What size do you want? Small, Medium, or Large? ")
pepperoni = input("Do you want pepperoni? Yes or no? ")
extra_cheese = input("Do you want extra cheese? Yes or no? ")
price = 0

if size == "Small":
    price += 10
    if pepperoni == "Yes":
        price += 2
elif size == "Medium":
    price += 15
    if pepperoni == "Yes":
        price += 3
elif size == "Large":
    price += 20
    if pepperoni == "Yes":
        price += 3

if extra_cheese == "Yes":
    price += 1
    
print(f"That pizza will cost you ${price}.")
