"""File to define Fish class"""

__author__ = "730704135"


class Fish:
    """Class to create a Fish."""
    age: int
    def __init__(self):
        """init function."""
        self.age = 0
        return None
    
    def one_day(self):
        """one_day function."""
        self.age += 1
        return None