print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What tip percentage would you like to give? "))

NumPeople = int(input("How many people to split the bill? "))


tip_as_percent = tip / 100

tip_actual = tip_as_percent * bill

BillWithTip = tip_actual + bill

bill_split = BillWithTip / NumPeople

bill_split_rounded = round(bill_split, 2)

print(f"Each person should pay ${bill_split_rounded}")
