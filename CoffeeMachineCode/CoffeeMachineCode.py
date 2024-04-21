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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficent(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    # is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            # is_enough = False
            return False
    # return is_enough
    return True

def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickless?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_succesful(money_recived, drink_cost):
    """ Return True when the payment is accepted, or False if money is insufficient."""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the current resoures"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is yout {drink_name}")

coffee_names = []
def coffee_Name(coffee_names):
    for i in MENU.keys():
        coffee_names.append(i)
    return coffee_names

coffee_name = coffee_Name(coffee_names)

coffeeMachine_on = True

while coffeeMachine_on:
    choice = input(f"What would you like? {', ' .join(coffee_name)} : ").lower()
    if choice == 'off':
        coffeeMachine_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])

