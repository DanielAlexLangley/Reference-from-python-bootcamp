# TODO A few bugs below. Mainly the program loops when it shouldn't inside the if statement(s)


MENU = {
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


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f'Water:   {resources["water"]}ml')
    print(f'Milk:    {resources["milk"]}ml')
    print(f'Coffee:  {resources["coffee"]}g')
    print(f'Money:  ${MONEY}')
    main_process()


def resource_check(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry. There is not enough {item}.")
            main_process()                                # TODO bug - restarts while still in loop


def collecting_coins(choice):
    print("Please insert coins.")
    coins = 0.0
    coins += float(input("How many quarters? ")) * .25
    coins += float(input("How many dimes? ")) * .1
    coins += float(input("How many nickles? ")) * .05
    coins += float(input("How many pennies? ")) * .01
    if coins < MENU[choice]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        main_process()
    return coins


def transaction(coins, choice, drink):
    global MONEY
    change = round((coins - drink["cost"]), 2)
    MONEY += drink["cost"]
    print(
        f"Here is ${change} in change."
    )  # TODO this needs to be converted to always be $x.00 rather than just .0
    print(f"Here is your {choice}. Enjoy!")
    resource_change(drink["ingredients"])
    main_process()


def resource_change(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


def main_process():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Coffee machine program has shut off.")
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        resource_check(drink["ingredients"])
        transaction(collecting_coins(choice), choice, drink)


MONEY = 0.0
main_process()
