class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

"""
In this file (menu.py) we have 
Class:
-----
Two Classes is there:
1. MenuItem Class
2. Menu Class

Attributes:
----------

In the MenuItem Class Attributes is there:
- name 
(str) The name of the drink
e.g "latte"

- cost
(float) The price of the drink
e.g 1.5

- ingredients
(dictionary) The ingredients and amounts required to make the drink
{e.g {"water" : 100, "coffee" : 16}}

Methods:
-------

In the Menu Class Methods is there:

- get_items()
Returns all the names of the available menu items as a concatenated string.
e.g. “latte/espresso/cappuccino”

- find_drink(order_name)
Parameter order_name: (str) The name of the drinks order.
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
otherwise returns None.

"""