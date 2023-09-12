from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import MenuItem, Menu

coffee_menu = Menu()
# created an object under Menu class called coffee_menu.
my_menu = coffee_menu.get_items()
customer_order = coffee_menu.find_drink("latte")
print(my_menu)
print(customer_order.ingredients)

coffee_making = CoffeeMaker()
okay_coffee = coffee_making.is_resource_sufficient(customer_order)
print(okay_coffee)

coins_me = MoneyMachine()
checking = coins_me.make_payment(customer_order.cost)
print(checking)
final_report = coins_me.report()
print(final_report)
coffee_ready = CoffeeMaker.make_coffee(customer_order)
print(coffee_ready)