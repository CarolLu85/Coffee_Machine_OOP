class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }
    def get_menu(self):
        return self.menu

    def get_cost(self, customer_choice):
        if customer_choice in self.menu:
            return self.menu[customer_choice]["cost"]
    # my understanding of having this get_menu function is that to make the actual menu visible to customers/outsiders via print statement. otherwise, it will be just a attribute inside the class.

    def resources_checking(self, customer_choice):
        for ingredient in self.menu[customer_choice]["ingredients"]:
            if self.menu[customer_choice]["ingredients"][ingredient] > self.resources[ingredient]:
                return False
        return True

    def coffee_making(self, customer_choice):
        print(f"here is your {customer_choice}! Enjoy")
        for ingredient_quantity in self.menu[customer_choice]["ingredients"]:
            self.resources[ingredient_quantity] = self.resources[ingredient_quantity] - self.menu[customer_choice]["ingredients"][ingredient_quantity]

