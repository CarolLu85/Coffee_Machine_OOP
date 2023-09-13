from my_own_version_money import DealingMoney
from my_own_version_coffee_machine import CoffeeMachine


coffee_menu = CoffeeMachine()
coffee_payment = DealingMoney()
coffee_machine_on = True

while coffee_machine_on:
    menu = coffee_menu.get_menu()
    customer_choice = input("what would you like? (Latte/Espresso/Cappuccino)")
    cost = coffee_menu.get_cost(customer_choice)
    if customer_choice == "off":
        coffee_machine_on = False
    else:
        if coffee_menu.resources_checking(customer_choice) == True:
            coffee_payment.insert_coins()
            if coffee_payment.money_checking(cost):
                coffee_menu.coffee_making(customer_choice)





