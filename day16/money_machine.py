class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        total = 0

        for coin in self.COIN_VALUES:
            total += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        return total

    def make_payment(self, cost):
        print("Please insert coins.")
        payment = self.process_coins()

        if payment >= cost:
            change = round(payment - cost, 2)

            if change > 0:
                print(f"Here is ${change} in change.")

            self.profit += cost
            return True

        print("Sorry that's not enough money. Money refunded.")
        return False