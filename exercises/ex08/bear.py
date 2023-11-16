"""File to define Bear class."""


__author__ = "730704135"


class Bear:
    """Class to create a bear."""
    age: int
    hunger_score: int

    def __init__(self):
        """Init."""
        self.age = 0
        self.hunger_score = 0
        """Init."""
        return None
    
    def one_day(self):
        """One_day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Beat Eat."""
        self.hunger_score += num_fish
        return None