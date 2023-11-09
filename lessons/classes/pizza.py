"""Defining a class!"""

from __future__ import annotations

class Pizza:

    # attributes
    # think of these as the variables each instance of my class will have
    # <name> : <type>
    size : str
    toppings : int
    gluten_free : bool

    def __init__(self, input_size: str, input_toppings: int, input_gf: bool):
        """My constructor."""
        self.size = input_size
        self.toppings = input_toppings
        self.gluten_free = input_gf
        # returns a Pizza object
    
    def price(self) -> float:
        """Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int):
        """Add toppings to existing pizza."""
        self.toppings += num_toppings
    
    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizzas's properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza

class Cereal:
    cereal: str
    def choose(type_cereal:str):
        return type_cereal
    