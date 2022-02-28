
# I am only supposed to edit coffee_machine_oop_main.py.
# I am not supposed to edit:
# coffee_machine_oop_coffee_maker.py
# coffee_machine_oop_menu.py, or...
# coffee_machine_oop_money_machine.py.
# I am supposed to treat those 3 py files like an external library.
# I am not even really supposed to look in there and learn what they do...
# ...except I should look at and use the documentation to understand and use them.
# See PDF with instructions from Day 16 of the python bootcamp course:
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19914252


from coffee_machine_oop_menu import Menu, MenuItem
from coffee_machine_oop_coffee_maker import CoffeeMaker
from coffee_machine_oop_money_machine import MoneyMachine


object_menu = Menu()
object_coffee_maker = CoffeeMaker()
object_money_machine = MoneyMachine()

is_on = True

while is_on:
    drink = input(f"\nWhat would you like? {object_menu.get_items()}: \n")
    if drink == "off":
        print("Coffee machine program has shut off.")
        is_on = False
    elif drink == "report":
        object_coffee_maker.report()
        object_money_machine.report()
    else:
        menu_item = object_menu.find_drink(drink)
        if object_coffee_maker.is_resource_sufficient(menu_item) and object_money_machine.make_payment(menu_item.cost):
            object_coffee_maker.make_coffee(menu_item)
