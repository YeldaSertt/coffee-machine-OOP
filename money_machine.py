from time import sleep


class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.seccions = False

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def _money_calc(self):
        print("Please insert coins.")
        for key,value in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {key} :  ")) * self.COIN_VALUES[key]
        return self.money_received


    def make_payment(self, cost):
        glass_yes_or_no = input("Would you like to enlarge your glass selection?? yes/no  : ").strip().lower()
        self._money_calc()
        if glass_yes_or_no == "yes":
            if self.money_received >= cost:
                self.money_received = GlassSelection().add_money_glass()
                money_control = round(self.money_received - cost,2)
                self.profit += money_control
                self.money_received = 0

                return True

            else:
                print("Sorry that's not enough money. Money refunded.")
                self.money_received = 0
                return False
        else:
            if self.money_received >= cost:
                money_control = round(self.money_received - cost,2)
                self.profit += money_control
                self.money_received = 0
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                self.money_received = 0
                return False

class GlassSelection(MoneyMachine):
    def __init__(self):
        self.new_cost = 0
        self.glass = {
            "grande" : 0.50,
            "little" : 0.25,
        }
    def add_money_glass(self):

        options = ""
        for item in self.glass:
            options += f"{item}/"
        glass_selection = self.glass[input(f" Write down the cup size ==>> {options}")]
        self.new_cost =  MoneyMachine._money_calc() + glass_selection
        return self.new_cost

