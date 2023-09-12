from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu

# created an object under each class.
coffee_menu = Menu()
coffee_maker= CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True
while coffee_machine_on:
    coffees_can_be_made_by_this_machine = coffee_menu.get_items()
    choice = input(f"What would you like? {coffees_can_be_made_by_this_machine}:")
    if choice == "off":
        coffee_machine_on = False
    elif (choice == "report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



