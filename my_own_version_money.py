class DealingMoney:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.payment_received = 0
        self.profit = 0


    def insert_coins(self):
        for coins in self.COIN_VALUES:
            self.payment_received += int(input(f"How many {coins}: ? \n")) * \
                                            self.COIN_VALUES[coins]
        return self.payment_received

    def money_checking(self, cost):

        if self.payment_received >= cost:
            changes = self.payment_received - cost
            print(f"Here is your ${round(changes, 2)} changes")
            self.profit += cost
            self.payment_received = 0
            return True
        else:
            print("That's not enough money. Sorry! Money refunded!")
            return False