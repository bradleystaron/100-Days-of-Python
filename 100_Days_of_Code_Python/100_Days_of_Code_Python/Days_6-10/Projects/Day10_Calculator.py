def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    number1 = float(input("What is the first number? "))

    while should_accumulate:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        number2 = float(input("What is the second number? "))

        if operator == "+":
            answer = operations["+"](number1, number2)
            print(f"{number1} + {number2} = {answer}")
        elif operator == "-":
            answer = operations["-"](number1, number2)
            print(f"{number1} - {number2} = {answer}")
        elif operator == "*":
            answer = operations["*"](number1, number2)
            print(f"{number1} * {number2} = {answer}")
        elif operator == "/":
            answer = operations["/"](number1, number2)
            print(f"{number1} / {number2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")

        if choice == "y":
            number1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()