import menu
import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

latte = MenuItem(name="latte", cost=MENU["latte"]["cost"], water=MENU["latte"]["ingredients"]["water"], coffee=MENU["latte"]["ingredients"]["coffee"], milk=MENU["latte"]["ingredients"]["milk"])
espresso = MenuItem(name="espresso", cost=MENU["espresso"]["cost"], water=MENU["espresso"]["ingredients"]["water"], coffee=MENU["espresso"]["ingredients"]["coffee"], milk=MENU["espresso"]["ingredients"]["milk"])
cappuccino = MenuItem(name="cappuccino", cost=MENU["cappuccino"]["cost"], water=MENU["cappuccino"]["ingredients"]["water"], coffee=MENU["cappuccino"]["ingredients"]["coffee"], milk=MENU["cappuccino"]["ingredients"]["milk"])

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while 1:

    preference = input('''
    What would you like espresso, latte or cappuccino?
    please type:
    1 for espresso or "espresso"
    2 for latte or "latte"
    3 for cappuccino or "cappuccino"
    4 to report the resources or "report"
    5 to turn off the machine or "off"

    i am happily waiting for your choose:
    ''')

    if preference == '1' or preference == 'espresso':
        if my_coffee_maker.is_resource_sufficient(espresso):
            if my_money_machine.make_payment(cost=espresso.cost):
                my_coffee_maker.make_coffee(espresso)
                print(f"“Here is your {espresso.name}. Enjoy!”")
        else:
            print("Sorry there is not enough resources")
    elif preference == '2' or preference == "latte":
        if my_coffee_maker.is_resource_sufficient(latte):
            if my_money_machine.make_payment(cost=latte.cost):
                my_coffee_maker.make_coffee(latte)
                print(f"“Here is your {latte.name}. Enjoy!”")
        else:
            print("Sorry there is not enough resources")
    elif preference == '3' or preference == 'cappuccino':
        if my_coffee_maker.is_resource_sufficient(cappuccino):
            if my_money_machine.make_payment(cost=cappuccino.cost):
                my_coffee_maker.make_coffee(cappuccino)
                print(f"“Here is your {cappuccino.name}. Enjoy!”")
        else:
            print("Sorry there is not enough resources")
    elif preference == '4' or preference == 'report':
        os.system("cls")
        my_coffee_maker.report()
        my_money_machine.report()
    elif preference == '5' or preference == 'off':
        break
    else:
        print("sorry choose one of the proper choices")

