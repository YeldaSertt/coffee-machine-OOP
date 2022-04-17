from time import sleep


class MenuItem:
    def __init__(self,name,water,coffee,milk,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "coffee" : coffee,
            "milk" : milk
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):

        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self,options):

        for item in self.menu:
            if item.name == options:
                return item
        print("Sorry that item is not available.")


