from time import sleep
from pyfiglet import Figlet

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import  MoneyMachine

def welcome():
    f = Figlet(font='cybermedium')
    print(f'''\033[33m
             )))
            (((
          +-----+
          |     |] -  WELCOME TO THE COFFEE MACHINE!          
          `-----'  
          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------

          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')


machine_case = True
menu =  Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while machine_case:
    welcome()
    options = menu.get_items()
    user_choice = str(input(f" What would you like\n Options =>> {options} : ")).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        machine_case=False

    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
        sleep(10)

    elif menu.find_drink(user_choice) is None:
        print('\033[31mError. Please choose an available option.\033[m')
    else:
        beverage = menu.find_drink(user_choice)
        print(beverage)
        sufficient_resources = coffee_maker.is_resource_sufficient(beverage)
        money_resources = money_machine.make_payment(beverage.cost)
        if sufficient_resources and money_resources:
            print('Done! Allow us to make your beverage now.')
            coffee_maker.make_coffee(beverage)

        off = input("Will you take another action? yes/no :  ").lower().strip()

        if off == "yes":
            machine_case = True

        elif off =="no":
            print("Good a hava day 👋")
            sleep(25)

