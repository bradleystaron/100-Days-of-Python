from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

Coffee_Machine_is_On = True

while Coffee_Machine_is_On:
    options = menu.get_items()
    user_choice = (input(f"What would you like? ({options}): ")).lower()
    
    if user_choice == "off":
        Coffee_Machine_is_On = False
        
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)