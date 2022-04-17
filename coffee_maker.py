
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def __report(self):

        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self,drink):

        can_make = True
        for key, value in drink.ingredients.items():
            if drink.ingredients[key] > self.resources[key]:
                print(f"Sorry there is not enough {key}.")
                can_make = False

        return can_make

    def make_coffee(self,order):

        for key,value in order.ingredients.items():
            self.resources[key] -= order.ingredients[key]
        print(f"Here is your {order.name} ☕. Enjoy!")
