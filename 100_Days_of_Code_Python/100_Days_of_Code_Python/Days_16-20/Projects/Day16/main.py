from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()

Coffee_Machine_is_On = True

while Coffee_Machine_is_On:
    user_input = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if user_input == "off":
        Coffee_Machine_is_On = False
    elif user_input == "report":
        Coffee_Maker.report()
        Money_Machine.report()
    else:
        drink = Menu.find_drink(user_input)
        if Coffee_Maker.is_resource_sufficient(drink) and Money_Machine.make_payment(drink.cost):
            Coffee_Maker.make_coffee(drink)